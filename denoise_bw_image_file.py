import os
import cv2
import numpy as np
from create_dir_before_write_file import create_dir_before_write_file


def denoise_bw_image_file(bw_image_with_white_noise_file_path, denoised_bw_image_file_path, kernel_size_1, kernel_size_2):
    color_image = cv2.imread(bw_image_with_white_noise_file_path)
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    threshold_value, bw_image = cv2.threshold(
        gray_image, 254, 255, cv2.THRESH_BINARY)
    kernel = np.ones((kernel_size_1, kernel_size_2), np.uint8)
    denoised_bw_image = cv2.morphologyEx(bw_image, cv2.MORPH_OPEN, kernel)
    create_dir_before_write_file(denoised_bw_image_file_path)
    cv2.imwrite(denoised_bw_image_file_path, denoised_bw_image)
