import csv
import os
from rich.console import Console
from rich.table import Table
from add_intent import intent_check, add_intent
from add_parameter import parameter_check, add_parameter
from intent_parameter_linkage import link_intent


def status_table(items: list, item_type: str, title: str):
    """
        Display a status table using the rich library.

        Args:
            items (list): List of tuples containing item name and line number.
            item_type (str): Type of the items (e.g., 'intent', 'parameter').
            title (str): Title of the table.
        """
    table = Table(title=title)
    table.add_column(item_type, style="cyan", no_wrap=True)
    table.add_column('LINE', style="magenta")

    for item in items:
        table.add_row(item[0], str(item[1]))

    Console().print(table)


def operation_check(file_path: str) -> str:
    """
        Check the type of CSV file based on its header.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            str: Type of the CSV file ('INTENT', 'INTENT_PARAMETER', or 'PARAMETER').
        """
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        first_line = next(csv_reader)
        if first_line == ['name', 'examples', 'description']:
            return 'INTENT'
        elif first_line == ['intent', 'parameter', 'necessary']:
            return 'INTENT_PARAMETER'
        else:
            return 'PARAMETER'


def duplicate_check(file_path: str, item_type: str) -> bool:
    """
        Check for items in the CSV file that could lead to duplicate in the database.

        Args:
            file_path (str): Path to the CSV file.
            item_type (str): Type of items to check ('INTENT' or 'PARAMETER').

        Returns:
            bool: True if no duplicates are found, False otherwise.
        """
    duplicate_list = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for count, line in enumerate(csv_reader, start=2):
            if item_type == "INTENT":
                status = intent_check(line[0])
            else:
                status = parameter_check(line[0])
            if status[0]:
                duplicate_list.append((line[0], count))

    if duplicate_list:
        print(f"\n\nSome {item_type.lower()} that are in the file already exist in the database:\n\n")
        status_table(duplicate_list, item_type, "")
        return False
    return True


def check_path(path):
    """
        Check if the specified path exists.

        Args:
            path (str): Path to check.

        Returns:
            bool: True if the path exists, False otherwise.
        """
    return os.path.exists(path)


def match_check(file_path: str):
    """
        Check if all intents and parameters in the file exist in the database.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            bool: True if all intents and parameters exist, False otherwise.
        """
    non_existent_parameters = []
    non_existent_intents = []

    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for count, line in enumerate(csv_reader, start=2):
            if not intent_check(line[0])[0]:
                non_existent_intents.append((line[0], count))
            if not parameter_check(line[1])[0]:
                non_existent_parameters.append((line[1], count))

    if non_existent_intents or non_existent_parameters:
        print('\n\nSome parameters or intents in the file do not exist in the database:\n\n')
        status_table(non_existent_intents, 'intent', "")
        status_table(non_existent_parameters, 'parameter', "")
        return False
    return True


def add_file(file_path: str, item_type: str):
    """
        Add intents, parameters, or intent-parameter linkages from a CSV file to the database.

        Args:
            file_path (str): Path to the CSV file.
            item_type (str): Type of items to add ('INTENT', 'PARAMETER', or 'INTENT_PARAMETER').
        """
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        if item_type == "INTENT":
            for line in csv_reader:
                intent = {
                    "name": line[0],
                    "examples": line[1].split(';'),
                    "description": line[2]
                }
                add_intent(intent)
        elif item_type == "PARAMETER":
            for line in csv_reader:
                parameter = {
                    "name": line[0],
                    "description": line[1],
                    "format": ",".join(line[2:])
                }
                add_parameter(parameter)
        else:
            bool_dict = {'true': True, 'false': False}
            for line in csv_reader:
                intent_parameter = {
                    "intent": line[0],
                    "parameter": line[1],
                    "necessary": bool_dict[line[2].lower()]
                }
                link_intent(intent_parameter)
