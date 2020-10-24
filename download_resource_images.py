import time
from download_file import download_file
from create_dir import create_dir
from get_year_month_from_url import get_year_month_from_url


def download_resource_images(url_list, dst_path):
    for url in url_list:
        dst_dir_path = dst_path + "/" + get_year_month_from_url(url)
        create_dir(dst_dir_path)
        dst_file_path = dst_dir_path + "/saizeriya_photo_hunt_original_image.png"
        download_file(url, dst_file_path)
        # time.sleep(5)
