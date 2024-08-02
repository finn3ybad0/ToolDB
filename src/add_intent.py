import json


FILE_PATH = '../data/intents.json'


def intent_check(intent: str) -> tuple[bool, int]:
    """
        Check if an intent exists in the JSON file.

        Args:
            intent (str): The name of the intent to check.

        Returns:
            Tuple[bool, int]: A tuple containing a boolean indicating if the intent exists,
                              and the index of the intent if it exists, otherwise -1.
        """
    try:
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)
        for index, element in enumerate(data["intents"]):
            if element['name'] == intent:
                return True, index
        return False, -1
    except FileNotFoundError:
        print("File not found.")
        return False, -1
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return False, -1


def add_intent(intent: dict) -> None:
    """
        Add a new intent to the JSON file.

        Args:
            intent (Dict): The intent dictionary to add.
        """
    try:
        with open(FILE_PATH, 'r+') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {"intents": []}
            data["intents"].append(intent)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except IOError as e:
        print(f"IOError: {e}")

