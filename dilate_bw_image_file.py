import os
import cv2
import numpy as np
from create_dir import create_dir


def dilate_bw_image_file(bw_image_file_path, dilated_bw_image_file_path, kernel_size_1, kernel_size_2, iteration_times):
    color_image = cv2.imread(bw_image_file_path)
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    threshold_value, bw_image = cv2.threshold(
        gray_image, 254, 255, cv2.THRESH_BINARY)
    kernel = np.ones((kernel_size_1, kernel_size_2), np.uint8)
    dilated_bw_image = cv2.dilate(bw_image, kernel, iterations=iteration_times)
    dilated_bw_image_path = os.path.dirname(dilated_bw_image_file_path)
    create_dir(dilated_bw_image_path)
    cv2.imwrite(dilated_bw_image_file_path, dilated_bw_image)
