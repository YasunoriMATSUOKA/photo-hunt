import os
import cv2
import numpy as np
from create_dir import create_dir


def erose_bw_image_file(bw_image_file_path, erosed_bw_image_file_path):
    color_image = cv2.imread(bw_image_file_path)
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    threshold_value, bw_image = cv2.threshold(
        gray_image, 254, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.unit8)
    erosed_bw_image = cv2.erode(bw_image, kernel, iterations=1)
    erosed_bw_image_path = os.path.dirname(erosed_bw_image_file_path)
    create_dir(erosed_bw_image_path)
    cv2.imwrite(erosed_bw_image_file_path, erosed_bw_image)
