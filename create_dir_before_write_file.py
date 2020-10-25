import os
from create_dir import create_dir


def create_dir_before_write_file(file_path):
    dir_path = os.path.dirname(file_path)
    create_dir(dir_path)
