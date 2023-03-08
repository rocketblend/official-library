import bpy
import os
import yaml
from addon_utils import modules

TAG = "preinstalled"
PACKAGEFILE = "rocketpack.yaml"

# Create a folder to store the addon YAML files
ROOTFOLDER = 'addons'
if not os.path.exists(ROOTFOLDER):
    os.mkdir(ROOTFOLDER)

# Get a list of addon module names
MODULES = [module.__name__ for module in modules()]

# Loop over each addon and write its name to a separate YAML file
for module_name in MODULES:
    addon_dict = {"addon": {"name": module_name}}

    # Determine the type of addon for the folder name
    addon_folder_category = None
    if bpy.utils.registered() == 'COMMUNITY':
        addon_folder_category = 'community'
    else:
        addon_folder_category = 'blender'

    # Write the addon dictionary to a YAML file in the appropriate folder
    addon_folder_name = os.path.join(ROOTFOLDER, addon_folder_category, addon_name, TAG)
    if not os.path.exists(addon_folder_name):
        os.mkdir(addon_folder_name)

    file_name = os.path.join(addon_folder_name, PACKAGEFILE)
    with open(file_name, 'w') as f:
        yaml.dump(addon_dict, f, default_flow_style=False)