import json


FILE_PATH = '../data/parameters.json'


def parameter_check(parameter: str) -> tuple[bool, int]:
    """
        Check if a parameter exists in the JSON file.

        Args:
            parameter (str): The name of the parameter to check.

        Returns:
            Tuple[bool, int]: A tuple containing a boolean indicating if the parameter exists,
                              and the index of the parameter if it exists, otherwise -1.
        """
    try:
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)
        for index, element in enumerate(data["parameters"]):
            if element['name'] == parameter:
                return True, index
        return False, -1
    except FileNotFoundError:
        print("File not found.")
        return False, -1
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return False, -1


def add_parameter(parameter: dict):
    """
        Add a new parameter to the JSON file.

        Args:
            parameter (Dict): The parameter dictionary to add.
        """
    try:
        with open(FILE_PATH, 'r+') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {"parameters": []}
            data["parameters"].append(parameter)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except IOError as e:
        print(f"IOError: {e}")


