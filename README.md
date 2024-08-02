# ToolDB : Database Management Tool

## Overview

This project is an interactive console application for managing entries of intents, parameters, and linking them. It provides functionalities to add, modify, and validate intents and parameters, import CSV files, and display relevant information.

## Features

- **Main Menu:** Navigate through various options to manage intents, parameters, and links.
- **Add Intent:** Create and validate new intents with examples and descriptions.
- **Add Parameter:** Create and validate new parameters with descriptions and formats.
- **Link Intent to Parameter:** Establish relationships between intents and parameters, marking them as necessary or optional.
- **Import CSV:** Validate and import intents and parameters from CSV files.
- **Modify Entries:** Edit existing intents, parameters, and links.
- **Validation and Preview:** Confirm and preview entries before finalizing changes.
- **Quit:** Exit the application.

## Setting Up the Development Environment

To get started with the project, you'll need to set up a Python virtual environment. This isolates your project's dependencies from the global Python installation.

useful resources : https://docs.python.org/3/library/venv.html

## Prerequisites

- Python 3.x
- Required Python packages: `rich`, `inquirer`

You can install the necessary packages using pip:
```bash
pip install rich inquirer
```
or

```bash
pip install -r requirements.txt
```

## IMPORTANT

Before you begin, ensure you have the following setup:

### Code Configuration

**This step is crucial for the code to function correctly.** You must configure certain paths in the code as follows:

- **Set the Import Folder Path**:
  - Open `ToolDB.py`.
  - Locate and set the `_ABSOLUTE_PATH_` variable to the path of the import folder where CSV files will be stored.

- **Set the JSON File Paths**:
  - Open `add_parameter.py`, `add_intent.py`, and `intent_parameter_linkage.py`.
  - Locate and set the `PATH_FILE` variable in each script to the path of the corresponding JSON file that stores relevant data.

**Failure to configure these paths correctly will prevent the application from running as intended.** Ensure these settings are accurate and reflect the actual locations of your files.



