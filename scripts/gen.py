import bpy

if bpy.app.background:
    import pip
    pip.main(['install', 'PyYAML'])

    import os
    import re
    import yaml
    from addon_utils import modules

    TAG = "pre-installed"
    PACKAGEFILE = "rocketpack.yaml"

    def make_friendly(s):
        s = s.replace(' ', '-')
        s = re.sub(r'[^\w-]', '', s)
        return s.lower()

    OUTPUT_DIR = os.path.join(os.path.dirname(bpy.data.filepath), 'packages')
    ADDONS_FOLDER = 'addons'

    # Loop over each addon and write its name to a separate YAML file
    for module in modules():
        addon_name = module.__name__
        addon_display_name = module.bl_info.get('name', addon_name)
        addon_dict = {"addon": {"name": module.__name__}}

        # Determine the type of addon for the folder name
        addon_folder_category = None
        addon_support = module.bl_info.get('support', "COMMUNITY")

        if addon_support == 'COMMUNITY':
            addon_folder_category = 'community'
        elif addon_support == 'OFFICIAL':
            addon_folder_category = 'blender'
        else:
            addon_folder_category = 'unknown'

        # Write the addon dictionary to a YAML file in the appropriate folder
        addon_folder_name = os.path.join(OUTPUT_DIR, addon_folder_category, ADDONS_FOLDER, make_friendly(addon_display_name), TAG)
        if not os.path.exists(addon_folder_name):
            os.makedirs(addon_folder_name)

        file_name = os.path.join(addon_folder_name, PACKAGEFILE)
        with open(file_name, 'w') as f:
            yaml.dump(addon_dict, f, default_flow_style=False)

    bpy.ops.wm.quit_blender()