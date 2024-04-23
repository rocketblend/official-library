import bpy

if bpy.app.background:
    import bpy
    import json
    import os
    import re
    from addon_utils import modules

    TAG = "pre-installed"
    PACKAGEFILE = "rocketpack.json"
    SPEC = "0.1.0"
    CATEGORIES = False

    def make_friendly(s):
        s = s.replace(' ', '-')
        s = re.sub(r'[^\w-]', '', s)
        return s.lower()

    OUTPUT_DIR = os.path.join(os.path.dirname(bpy.data.filepath), 'packages', 'v0')
    ADDONS_FOLDER = 'addons'

    # Loop over each addon and write its name to a separate JSON file
    for module in modules():
        addon_name = module.__name__
        addon_display_name = module.bl_info.get('name', addon_name)
        addon_dict = {
            "spec": SPEC,
            "type": "addon",
            "name": module.__name__,
        }

        # Determine the type of addon for the folder name
        addon_folder_category = None
        if CATEGORIES:
            addon_support = module.bl_info.get('support', "COMMUNITY")
            if addon_support == 'COMMUNITY':
                addon_folder_category = 'community'
            elif addon_support == 'OFFICIAL':
                addon_folder_category = 'blender'
            else:
                addon_folder_category = 'unknown'

        # Determine folder path with or without category
        if addon_folder_category:
            folder_path = os.path.join(OUTPUT_DIR, addon_folder_category, ADDONS_FOLDER, make_friendly(addon_display_name), TAG)
        else:
            folder_path = os.path.join(OUTPUT_DIR, ADDONS_FOLDER, make_friendly(addon_display_name), TAG)

        # Write the addon dictionary to a JSON file in the appropriate folder
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_name = os.path.join(folder_path, PACKAGEFILE)
        with open(file_name, 'w') as f:
            json.dump(addon_dict, f, indent=4)

    bpy.ops.wm.quit_blender()