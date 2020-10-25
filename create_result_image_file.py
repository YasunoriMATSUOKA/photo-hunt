import os
import cv2
from create_dir_before_write_file import create_dir_before_write_file


def create_result_image_file(diff_image_file_path, mask_image_file_path, single_result_image_file_path, result_image_file_path, left_image_file_path, right_image_file_path):
    diff_image = cv2.imread(diff_image_file_path)
    mask_image = cv2.imread(mask_image_file_path)
    result_image = cv2.bitwise_and(diff_image, mask_image)
    create_dir_before_write_file(single_result_image_file_path)
    cv2.imwrite(single_result_image_file_path, result_image)

    left_image = cv2.imread(left_image_file_path)
    right_image = cv2.imread(right_image_file_path)
    result_image = cv2.hconcat([result_image, left_image, right_image])
    create_dir_before_write_file(result_image_file_path)
    cv2.imwrite(result_image_file_path, result_image)
