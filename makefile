# Define the path to Blender's Python executable
# TODO: Add support for running scripts in RocketBlend. Temporary for now.
BLENDER_PYTHON := C:\Users\Elliot\AppData\Roaming\rocketblend\packages\github.com\rocketblend\official-library\builds\blender\stable\3.4.1\blender-3.4.1-windows-x64\3.4\python\bin\python.exe
BLENDER_EXECUTABLE := C:\Users\Elliot\AppData\Roaming\rocketblend\packages\github.com\rocketblend\official-library\builds\blender\stable\3.4.1\blender-3.4.1-windows-x64\blender.exe

# Define the path to your Python script
SCRIPT := gen.py

# Define the name of the virtual environment
VENV_NAME := venv

# Define the name of the requirements file
REQUIREMENTS_FILE := requirements.txt

DIR := ${CURDIR}

.PHONY: env
env:
	echo Installing the required packages
	$(BLENDER_PYTHON) -m ensurepip
	$(BLENDER_PYTHON) -m pip install --upgrade pip
	$(BLENDER_PYTHON) -m pip install -r $(REQUIREMENTS_FILE)

.PHONY: run
run:
	echo Running the Python script with Blender's Python executable
	$(BLENDER_EXECUTABLE) -b --python $(DIR)/$(SCRIPT)