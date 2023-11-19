import os

def get_assets_folder() -> str:
    working_dir = os.path.basename(os.getcwd())
    assets_folder = ""
    
    if working_dir == "app":
        assets_folder = os.path.join("UI", "assets")
    else:
        assets_folder = os.path.join("app", "UI", "assets")
    
    return assets_folder