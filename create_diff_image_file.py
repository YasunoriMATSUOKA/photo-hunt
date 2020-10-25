import os
import cv2
from create_dir_before_write_file import create_dir_before_write_file


def create_diff_image_file(left_image_file_path, right_image_file_path, diff_image_file_path):
    left_image = cv2.imread(left_image_file_path)
    right_image = cv2.imread(right_image_file_path)
    diff_image = cv2.absdiff(left_image, right_image)
    create_dir_before_write_file(diff_image_file_path)
    cv2.imwrite(diff_image_file_path, diff_image)
