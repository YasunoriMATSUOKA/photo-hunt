import os
import pprint
import time
import urllib.error
import urllib.request
from create_dir_before_write_file import create_dir_before_write_file


def download_file(url, dst_path):
    create_dir_before_write_file(dst_path)
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)
