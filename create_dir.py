import os


def create_dir(new_dir_path):
    os.makedirs(new_dir_path, exist_ok=True)
