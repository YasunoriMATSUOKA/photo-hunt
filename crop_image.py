import os
import cv2
from create_dir_before_write_file import create_dir_before_write_file


def crop_image(image_file_path, crop_image_file_path, crop_x_min, crop_x_max, crop_y_min, crop_y_max):
    image = cv2.imread(image_file_path)
    crop_image = image[crop_y_min:crop_y_max, crop_x_min:crop_x_max]
    create_dir_before_write_file(crop_image_file_path)
    cv2.imwrite(crop_image_file_path, crop_image)
