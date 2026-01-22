import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

def get_asset_image_path(image_name):
    return os.path.join(PROJECT_ROOT, "assets", "images", image_name)