import os
import cv2
import numpy as np
from create_dir import create_dir


def convert_color_image_file_to_bw_image_file_with_manual_threshold(color_image_file_path, bw_image_file_path, manual_threshold):
    color_image = cv2.imread(color_image_file_path)
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    threshold_value, bw_image = cv2.threshold(
        gray_image, manual_threshold, 255, cv2.THRESH_BINARY)
    bw_image_path = os.path.dirname(bw_image_file_path)
    create_dir(bw_image_path)
    cv2.imwrite(bw_image_file_path, bw_image)
