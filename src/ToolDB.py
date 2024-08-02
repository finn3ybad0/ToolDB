import sys
import inquirer
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from add_intent import intent_check
from add_intent import add_intent
from add_parameter import parameter_check, add_parameter
from intent_parameter_linkage import link_intent
from add_file import check_path, operation_check, duplicate_check, match_check, add_file

INTENT = {
    "name": "",
    "examples": [],
    "description": ""
}

PARAMETER = {
    "name": "",
    "description": "",
    "format": ""
}

INTENT_PARAMETER = {
    "intent": "",
    "parameter": "",
    "necessary": True
}

CSV_PATH: str = ""
CSV_TYPE: str = ""

ABSOLUTE_PATH: str = "/Users/finney/Desktop/ToolDB/test/csv/"

kryptic_logo = '''
██   ██ ██████  ██    ██ ██████  ████████ ██  ██████ 
██  ██  ██   ██  ██  ██  ██   ██    ██    ██ ██      
█████   ██████    ████   ██████     ██    ██ ██      
██  ██  ██   ██    ██    ██         ██    ██ ██      
██   ██ ██   ██    ██    ██         ██    ██  ██████       

DBTOOL version. 1.0                                                        
                                                        '''
good_bye = '''
██████╗ ██╗   ██╗███████╗    ███████╗ ██████╗ ██████╗     ███╗   ██╗ ██████╗ ██╗    ██╗    ██╗
██╔══██╗╚██╗ ██╔╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗    ████╗  ██║██╔═══██╗██║    ██║    ██║
██████╔╝ ╚████╔╝ █████╗      █████╗  ██║   ██║██████╔╝    ██╔██╗ ██║██║   ██║██║ █╗ ██║    ██║
██╔══██╗  ╚██╔╝  ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗    ██║╚██╗██║██║   ██║██║███╗██║    ╚═╝
██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║    ██║ ╚████║╚██████╔╝╚███╔███╔╝    ██╗
╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝     ╚═╝

DBTOOL version. 1.0                                                                                              
'''
search_error = '''
██╗  ██╗ ██████╗ ██╗  ██╗             
██║  ██║██╔═████╗██║  ██║             
███████║██║██╔██║███████║             
╚════██║████╔╝██║╚════██║             
     ██║╚██████╔╝     ██║    ██╗██╗██╗
     ╚═╝ ╚═════╝      ╚═╝    ╚═╝╚═╝╚═╝

something went wrong idk ..                                      
'''
match_error = '''
██╗  ██╗ ██████╗ ██████╗              
██║  ██║██╔═████╗╚════██╗             
███████║██║██╔██║ █████╔╝             
╚════██║████╔╝██║ ╚═══██╗             
     ██║╚██████╔╝██████╔╝    ██╗██╗██╗
     ╚═╝ ╚═════╝ ╚═════╝     ╚═╝╚═╝╚═╝

bad bad bad request , check your stuff ...                                      
'''
cooking = '''
 ██████  ██████   ██████  ██   ██ ██ ███    ██  ██████               
██      ██    ██ ██    ██ ██  ██  ██ ████   ██ ██                    
██      ██    ██ ██    ██ █████   ██ ██ ██  ██ ██   ███              
██      ██    ██ ██    ██ ██  ██  ██ ██  ██ ██ ██    ██              
 ██████  ██████   ██████  ██   ██ ██ ██   ████  ██████      ██ ██ ██ 
                                                                     
                                                                     
'''
added_successfully = '''
              888      888               888                                                            .d888          888 888               888 
              888      888               888                                                           d88P"           888 888               888 
              888      888               888                                                           888             888 888               888 
 8888b.   .d88888  .d88888  .d88b.   .d88888      .d8888b  888  888  .d8888b .d88b.  .d8888b  .d8888b  888888 888  888 888 888 888  888      888 
    "88b d88" 888 d88" 888 d8P  Y8b d88" 888      88K      888  888 d88P"   d8P  Y8b 88K      88K      888    888  888 888 888 888  888      888 
.d888888 888  888 888  888 88888888 888  888      "Y8888b. 888  888 888     88888888 "Y8888b. "Y8888b. 888    888  888 888 888 888  888      Y8P 
888  888 Y88b 888 Y88b 888 Y8b.     Y88b 888           X88 Y88b 888 Y88b.   Y8b.          X88      X88 888    Y88b 888 888 888 Y88b 888       "  
"Y888888  "Y88888  "Y88888  "Y8888   "Y88888       88888P'  "Y88888  "Y8888P "Y8888   88888P'  88888P' 888     "Y88888 888 888  "Y88888      888 
                                                                                                                                    888          
                                                                                                                               Y8b d88P          
                                                                                                                                "Y88P"           
'''
csv = '''
 ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░       ░▒▓█▓▒▒▓█▓▒░  
░▒▓█▓▒░       ░▒▓██████▓▒░ ░▒▓█▓▒▒▓█▓▒░  
░▒▓█▓▒░             ░▒▓█▓▒░ ░▒▓█▓▓█▓▒░   
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ ░▒▓█▓▓█▓▒░   
 ░▒▓██████▓▒░░▒▓███████▓▒░   ░▒▓██▓▒░    
                                         
                                         
'''
lgtm = '''
██╗      ██████╗████████╗███╗   ███╗
██║     ██╔════╝╚══██╔══╝████╗ ████║
██║     ██║  ███╗  ██║   ██╔████╔██║
██║     ██║   ██║  ██║   ██║╚██╔╝██║
███████╗╚██████╔╝  ██║   ██║ ╚═╝ ██║
╚══════╝ ╚═════╝   ╚═╝   ╚═╝     ╚═╝

You may proceed !                                    
'''


def do_nothing():
    """A placeholder function that performs no operation."""
    pass


def selection_menu(menu: list):
    """
       Display the selection menu and execute the associated function.

       Args:
           menu (list): A list containing menu options and related details.
       """
    clear()
    options = [inquirer.List('function', message=menu[0], choices=menu[4:])]
    execute_function(menu[2], menu[3])
    answer = inquirer.prompt(options)
    alias = tag_check(answer['function'], menu[1])
    if alias != "None":
        return selection_menu(option_dict[alias])
    return selection_menu(option_dict[answer['function']])


def execute_function(func, args):
    """
        Execute a given function with the provided arguments.

        Args:
            func (function): The function to be executed.
            args (list): The arguments to be passed to the function.
        """
    if func is do_nothing:
        return
    if args is not None:
        func(*args) if len(args) > 1 else func(args[0])
    else:
        func()


def tag_check(answer: str, tag: str):
    """
        Check and return the alias associated with a given answer and tag.

        Args:
            answer (str): The selected answer from the menu.
            tag (str): The tag associated with the menu.

        Returns:
            str: The alias associated with the answer and tag.
        """
    return tag_dict.get((answer, tag), 'None')


def quit_program():
    """Clear the screen, display a goodbye message, and exit the program."""
    clear()
    display(good_bye)
    sys.exit()


def intent_data_entry():
    """Collect and validate data for a new intent."""
    global INTENT
    display(cooking)
    INTENT['name'] = Console().input("\nEnter name: ")
    while intent_check(INTENT['name'])[0]:
        clear()
        display(match_error)
        Console().print("\nIntent already exists , try again ")
        INTENT['name'] = Console().input("\nEnter name: ")
    clear()
    display(cooking)
    Console().print("\nEnter examples (end with EOF / Ctrl-D):\n")
    examples_input = sys.stdin.read()
    formatted_example = examples_input.split("\n")
    INTENT['examples'] = formatted_example[:-1]
    clear()
    display(cooking)
    INTENT['description'] = Console().input("\n\nEnter description: ")
    data_entry_preview("intent", INTENT)


def push_intent():
    """Add the collected intent to the system."""
    global INTENT
    add_intent(INTENT)
    display(added_successfully)


def link_intent_to_parameter_entry():
    """Collect and validate data for linking an intent to a parameter."""
    bool_dict = {'true': True, 'false': False}
    global INTENT_PARAMETER
    display(cooking)

    INTENT_PARAMETER['intent'] = Console().input("Enter intent: ")

    while not intent_check(INTENT_PARAMETER['intent'])[0]:
        clear()
        display(search_error)
        if INTENT_PARAMETER['intent'] == "abort":
            selection_menu(option_dict['main menu'])
        Console().print("Intent does not exist\n\n")
        INTENT_PARAMETER['intent'] = Console().input("Enter valid intent: ")

    clear()
    INTENT_PARAMETER['parameter'] = Console().input("Enter parameter: ")

    while not parameter_check(INTENT_PARAMETER['parameter'])[0]:
        clear()
        display(search_error)
        if INTENT_PARAMETER['parameter'] == "abort":
            selection_menu(option_dict['main menu'])
        Console().print("parameter does not exist\n\n")
        INTENT_PARAMETER['parameter'] = Console().input("Enter valid parameter: ")
    clear()
    necessity = Console().input("Enter necessity: ")
    INTENT_PARAMETER['necessary'] = bool_dict[necessity.lower()]
    data_entry_preview("link", INTENT_PARAMETER)


def push_link():
    """Add the collected link between intent and parameter to the system."""
    global INTENT_PARAMETER
    link_intent(INTENT_PARAMETER)
    display(added_successfully)


def parameter_data_entry():
    """Collect and validate data for a new parameter."""
    global PARAMETER

    clear()
    display(cooking)

    PARAMETER['name'] = Console().input("Enter name: ")
    while parameter_check(PARAMETER['name'])[0]:
        clear()
        display(search_error)
        print("parameter already exist, try again")
        PARAMETER['name'] = Console().input("Enter name: ")

    clear()
    display(cooking)

    PARAMETER['description'] = Console().input("Enter description: ")

    clear()
    display(cooking)

    PARAMETER['format'] = Console().input("Enter format: ")
    data_entry_preview("parameter", PARAMETER)


def push_parameter():
    """Add the collected parameter to the system."""
    global PARAMETER
    add_parameter(PARAMETER)
    display(added_successfully)


def modify_entry(field: str, dicti: str):
    """
        Modify a specific field in the given dictionary (INTENT, PARAMETER, or INTENT_PARAMETER).

        Args:
            field (str): The field to be modified.
            dicti (str): The dictionary to be modified (INTENT, PARAMETER, or INTENT_PARAMETER).
        """
    global INTENT
    global PARAMETER
    global INTENT_PARAMETER

    if dicti == "INTENT":
        if field == 'name':
            clear()
            display(cooking)
            INTENT[field] = Console().input("Enter " + field + ": ")
            while intent_check(INTENT[field])[0]:
                clear()
                display(search_error)
                print("intent already exist , try again ")
                INTENT[field] = Console().input("Enter name: ")
        else:
            clear()
            display(cooking)
            INTENT[field] = Console().input("Enter " + field + ": ")

        clear()
        data_entry_preview('intent', INTENT)
    elif dicti == "PARAMETER":
        clear()
        display(cooking)
        PARAMETER[field] = Console().input("Enter " + field + ": ")
        clear()
        data_entry_preview('parameter', PARAMETER)
        pass
    else:
        clear()
        display(cooking)
        INTENT_PARAMETER[field] = Console().input("Enter " + field + ": ")
        clear()
        data_entry_preview('link', INTENT_PARAMETER)
        pass


def data_entry_preview(element_name: str, element: dict):
    """
        Display a preview of the data entry for verification.

        Args:
            element_name (str): The name of the element being previewed.
            element (dict): The dictionary containing the element's data.
        """
    print(20 * '\n')
    panel1 = Panel(Align.center('[bold]' + element_name + ' preview[/bold]', vertical="middle"),
                   width=75, height=3, border_style="bold blue")
    Console().print(panel1)
    for key, value in element.items():
        if isinstance(value, list):
            formatted_example = "\n".join(value)
            panel2 = Panel(Align.center(formatted_example, vertical="middle"),
                           title=key, width=75, height=10, border_style="bold magenta")
        else:
            panel2 = Panel(Align.center(value, vertical="middle"),
                           title=key, width=75, height=6 if key == "description" else 3,
                           border_style="bold magenta")
        Console().print(panel2)


def investigate_file():
    """
        Prompt the user to enter the name of a CSV file, validate the file's existence and type,
        and navigate to the appropriate menu and function based on the validation results.

        This function performs the following steps:
        1. Displays initial instructions and prompts the user to input the CSV file name.
        2. Checks if the inputted file exists in the specified directory.
        3. Validates the type of CSV file (INTENT, PARAMETER, or other).
        4. Navigates to a specific menu and function based on the type and validation results of the file.
        """
    global CSV_PATH
    global CSV_TYPE

    display(csv)
    Console().print(" put the file in the csv folder \n\n")
    path = Console().input("Enter file name : ")

    CSV_PATH = ABSOLUTE_PATH + path + '.csv'  ## ADJUST HERE

    if path == 'abort':
        selection_menu(option_dict['main menu'])
    while not check_path(CSV_PATH):

        clear()
        display(search_error)
        Console().print("\npath is invalid, make sure the file is in the right folder or that the file is well typed\n")
        path = Console().input("Enter file name : ")
        CSV_PATH = ABSOLUTE_PATH + path + '.csv'

        if path == 'abort':
            selection_menu(option_dict['main menu'])

    clear()
    display(csv)
    file_type = operation_check(CSV_PATH)  ## ADJUST HERE
    CSV_TYPE = file_type

    if file_type == 'INTENT' or file_type == 'PARAMETER':
        if duplicate_check(CSV_PATH, file_type):
            selection_menu(option_dict['valid csv'])
    else:
        if match_check(CSV_PATH):
            selection_menu(option_dict['valid csv'])


def push_file():
    """
        Add the validated CSV file to the system and display a success message.
        """
    add_file(CSV_PATH, CSV_TYPE)
    display(added_successfully)


def clear():
    """
     Clear the console screen by printing 50 new lines.
     """
    print(50 * '\n')


def display(text: str):
    """
        Display the given text in a styled panel on the console.

        Args:
            text (str): The text to be displayed.
        """
    panel = Panel('[blue]' + text + '[/blue]', title="", expand=False, border_style="green")
    Console().print(panel)


# Tag dictionary
tag_dict = {
    ("yes", "add_intent_tag"): 'confirm intent',
    ("cancel", "add_intent_tag"): "main menu",
    ("modify", "add_intent_tag"): "modify intent",

    ("yes", "add_parameter_tag"): 'confirm parameter',
    ("cancel", "add_parameter_tag"): "main menu",
    ("modify", "add_parameter_tag"): "modify parameter",

    ("yes", "link_parameter_tag"): 'confirm link',
    ("cancel", "link_parameter_tag"): "main menu",
    ("modify", "link_parameter_tag"): "modify link",

    ("yes", "add_csv_tag"): 'confirm import',
    ("cancel", "add_csv_tag"): "main menu",

    ('yes', 'intent_validation_tag'): "confirm intent",
    ('cancel', 'intent_validation_tag'): "main menu",
    ('modify', 'intent_validation_tag'): "modify intent",

    ('yes', 'parameter_validation_tag'): "confirm parameter",
    ('cancel', 'parameter_validation_tag'): "main menu",
    ('modify', 'parameter_validation_tag'): "modify parameter",

    ('yes', 'link_validation_tag'): "confirm link",
    ('cancel', 'link_validation_tag'): "main menu",
    ('modify', 'link_validation_tag'): "modify link",

    ('validate change', 'modify_intent_tag'): "confirm intent",
    ('validate change', 'modify_parameter_tag'): "confirm parameter",
    ('validate change', 'modify_link_tag'): "confirm link",

    ('modify name', 'modify_menu_intent_tag'): "modify intent name",
    ('modify examples', 'modify_menu_intent_tag'): "modify intent examples",
    ('modify description', 'modify_menu_intent_tag'): "modify intent description",

    ('modify name', 'modify_menu_parameter_tag'): "modify parameter name",
    ('modify description', 'modify_menu_parameter_tag'): "modify parameter description",
    ('modify format', 'modify_menu_parameter_tag'): "modify parameter format",

    ('modify intent', 'modify_menu_link_tag'): "modify link intent",
    ('modify parameter', 'modify_menu_link_tag'): "modify link parameter",
    ('modify necessity', 'modify_menu_link_tag'): "modify link necessity",

    ('cancel', 'modify_intent_tag'): "validation intent",
    ('cancel', 'modify_parameter_tag'): "validation parameter",
    ('cancel', 'modify_link_tag'): "validation link",

    ('cancel', 'modify_menu_intent_tag'): "validation intent",
    ('cancel', 'modify_menu_parameter_tag'): "validation parameter",
    ('cancel', 'modify_menu_link_tag'): "validation link",

    ('add another intent', 'modify_menu_intent_tag'): "add intent",
    ('add another parameter', 'modify_menu_parameter_tag'): "add parameter",
    ('link another parameter', 'modify_menu_link_tag'): "add link",

    ('add another intent', 'add_intent_tag'): "add intent",
    ('add another parameter', 'add_parameter_tag'): "add parameter",
    ('link another parameter', 'link_parameter_tag'): "add link",

    ('add another file', 'add_csv_tag'): "import csv",

    ('back to main menu', "add_intent_tag"): "main menu",
    ('back to main menu', "add_parameter_tag"): "main menu",
    ('back to main menu', "add_link_tag"): "main menu",
    ('back to main menu', "add_csv_tag"): "main menu",
}

# Option dictionary
option_dict = {
    'main menu': ['select an option',  # text to display (instructions)
                  'main_menu_tag',  # tag
                  display,  # Function to launch
                  [kryptic_logo],  # Parameter for the function
                  'add intent',  # options to display
                  'add parameter',
                  'add link',
                  'import csv',
                  'quit'],
    'add intent': ['confirm ?',
                   'add_intent_tag',
                   intent_data_entry,
                   None,
                   'yes',
                   'modify',
                   'cancel'],
    'confirm intent': ['',
                       'add_intent_tag',
                       push_intent,
                       None,
                       'add another intent',
                       'back to main menu'],
    'validation intent': ['confirm ?',  # follows modification
                          'intent_validation_tag',
                          data_entry_preview,
                          ("intent", INTENT),
                          None,
                          'yes',
                          'modify',
                          'cancel'],
    'modify intent': ['select option to modify',
                      'modify_menu_intent_tag',
                      do_nothing,
                      None,
                      'modify name',
                      'modify examples',
                      'modify description',
                      'cancel'],
    'modify intent name': ['this is the preview',
                           'modify_intent_tag',
                           modify_entry,
                           ('name', 'INTENT'),
                           'validate change',
                           'cancel'],
    'modify intent examples': ['',
                               'modify_intent_tag',
                               modify_entry,
                               ('examples', 'INTENT'),
                               'validate change',
                               'cancel'],
    'modify intent description': ['',
                                  'modify_intent_tag',
                                  modify_entry,
                                  ('description', 'INTENT'),
                                  'validate change',
                                  'cancel'],
    "add parameter": ['confirm ?',
                      'add_parameter_tag',
                      parameter_data_entry,
                      None,
                      'yes',
                      'modify',
                      'cancel'],
    'confirm parameter': ['',
                          'add_parameter_tag',
                          push_parameter,
                          None,
                          'add another parameter',
                          'cancel'],
    'modify parameter': ['',
                         'modify_menu_parameter_tag',
                         do_nothing,
                         None,
                         'modify name',
                         'modify description',
                         'modify format'],
    'validation parameter': ['confirm ?',
                             'parameter_validation_tag',
                             data_entry_preview,
                             ('parameter', PARAMETER),
                             'yes',
                             'modify',
                             'cancel'],
    'modify parameter name': ['',
                              'modify_parameter_tag',
                              modify_entry,
                              ('name', 'PARAMETER'),
                              'validate change',
                              'cancel'],
    'modify parameter description': ['',
                                     'modify_parameter_tag',
                                     modify_entry,
                                     ('description', 'PARAMETER'),
                                     'validate change',
                                     'cancel'],
    'modify parameter format': ['',
                                'modify_parameter_tag',
                                modify_entry,
                                ('format', 'PARAMETER'),
                                'validate change',
                                'cancel'],
    'add link': ['confirm ?',
                 'link_parameter_tag',
                 link_intent_to_parameter_entry,
                 None,
                 'yes',
                 'modify',
                 'cancel'],
    'confirm link': ['',
                     'link_parameter_tag',
                     push_link,
                     None,
                     'link another parameter',
                     'cancel'],
    'modify link': ['',
                    'modify_menu_link_tag',
                    do_nothing,
                    None,
                    'modify intent',
                    'modify parameter',
                    'modify necessity'],
    'validation link': ['confirm ?',
                        'link_validation_tag',
                        data_entry_preview,
                        ('link', INTENT_PARAMETER),
                        'yes',
                        'modify',
                        'cancel'],
    'modify link intent': ['',
                           'modify_link_tag',
                           modify_entry,
                           ('intent', 'INTENT_PARAMETER'),
                           'validate change',
                           'cancel'],
    'modify link parameter': ['',
                              'modify_link_tag',
                              modify_entry,
                              ('parameter', 'INTENT_PARAMETER'),
                              'validate change',
                              'cancel'],
    'modify link necessity': ['',
                              'modify_link_tag',
                              modify_entry,
                              ('necessity', 'INTENT_PARAMETER'),
                              'validate change',
                              'cancel'],
    'import csv': ['',
                   'add_csv_tag',
                   investigate_file,
                   None,
                   'back to main menu'],
    'invalid csv': ['conflict',
                    'add_csv_tag',
                    do_nothing,
                    None,
                    'back to main menu'],
    'valid csv': ['confirm?',
                  'add_csv_tag',
                  display,
                  [lgtm],
                  'yes',
                  'cancel'],
    'confirm import': ['',
                       'add_csv_tag',
                       push_file,
                       None,
                       'add another file',
                       'back to main menu'],
    'quit': ['',
             'quit_tag',
             quit_program,
             None,
             '']

}

if __name__ == '__main__':
    panel = Panel(kryptic_logo, title="", expand=False, border_style="blue")
    Console().print(panel)
    selection_menu(option_dict["main menu"])
