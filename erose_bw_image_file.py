import os
import cv2
import numpy as np
from create_dir_before_write_file import create_dir_before_write_file


def erose_bw_image_file(bw_image_file_path, erosed_bw_image_file_path, kernel_size_1, kernel_size_2, iteration_times):
    color_image = cv2.imread(bw_image_file_path)
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    threshold_value, bw_image = cv2.threshold(
        gray_image, 254, 255, cv2.THRESH_BINARY)
    kernel = np.ones((kernel_size_1, kernel_size_2), np.uint8)
    erosed_bw_image = cv2.erode(bw_image, kernel, iterations=iteration_times)
    create_dir_before_write_file(erosed_bw_image_file_path)
    cv2.imwrite(erosed_bw_image_file_path, erosed_bw_image)
