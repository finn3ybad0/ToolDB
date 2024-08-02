import json

FILE_PATH = '../data/intent_parameter.json'


def link_intent(intent_parameter: dict):
    """
        Add a new intent-parameter linkage to the JSON file.

        Args:
            intent_parameter (Dict): The intent-parameter dictionary to add.
        """
    try:
        with open(FILE_PATH, 'r+') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {"intent_parameter": []}
            data["intent_parameter"].append(intent_parameter)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except IOError as e:
        print(f"IOError: {e}")
