# Define the path to Blender's Python executable
# TODO: Add support for running scripts in RocketBlend. Temporary for now.
BLENDER_PYTHON := C:\Users\Elliot\AppData\Roaming\rocketblend\packages\github.com\rocketblend\official-library\builds\blender\stable\3.4.1\blender-3.4.1-windows-x64\blender.exe

# Define the path to your Python script
SCRIPT := gen.py

# Define the name of the virtual environment
VENV_NAME := rb-library

# Define the name of the requirements file
REQUIREMENTS_FILE := requirements.txt

.PHONY: venv
venv:
	# Create a new virtual environment
	python3 -m venv $(VENV_NAME)

	# Activate the virtual environment
	source $(VENV_NAME)/bin/activate

	# Install the required packages
	pip install -r $(REQUIREMENTS_FILE)

.PHONY: run
run:
	# Activate the virtual environment
	source $(VENV_NAME)/bin/activate

	# Run the Python script with Blender's Python executable
	$(BLENDER_PYTHON) $(SCRIPT)