import os
import cv2
from create_dir import create_dir


def create_result_image_file(diff_image_file_path, mask_image_file_path, result_image_file_path, left_image_file_path, right_image_file_path):
    diff_image = cv2.imread(diff_image_file_path)
    mask_image = cv2.imread(mask_image_file_path)
    result_image = cv2.bitwise_and(diff_image, mask_image)
    left_image = cv2.imread(left_image_file_path)
    right_image = cv2.imread(right_image_file_path)
    result_image = cv2.hconcat([result_image, left_image, right_image])
    result_image_path = os.path.dirname(result_image_file_path)
    create_dir(result_image_path)
    cv2.imwrite(result_image_file_path, result_image)