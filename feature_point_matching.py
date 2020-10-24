import os
import numpy as np
import cv2
from create_dir import create_dir


def feature_point_matching(left_image_file_path, right_image_file_path, matching_result_image_file_path):
    left_image = cv2.imread(left_image_file_path)
    right_image = cv2.imread(right_image_file_path)

    akaze = cv2.AKAZE_create()
    kp_left, des_left = akaze.detectAndCompute(left_image, None)
    kp_right, des_right = akaze.detectAndCompute(right_image, None)

    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(des_left, des_right, k=2)

    ratio = 0.5
    good = []
    queryIdx_list = []
    trainIdx_list = []
    for m, n in matches:
        if m.distance < ratio * n.distance:
            good.append([m])
            queryIdx_list.append(m.queryIdx)
            trainIdx_list.append(m.trainIdx)

    matching_result_image = cv2.drawMatchesKnn(
        left_image,
        kp_left,
        right_image,
        kp_right,
        good,
        None,
        flags=2
    )

    matching_result_image_path = os.path.dirname(
        matching_result_image_file_path
    )
    create_dir(matching_result_image_path)
    cv2.imwrite(matching_result_image_file_path, matching_result_image)

    vector_x_list = []
    vector_y_list = []
    for queryIdx, trainIdx in zip(queryIdx_list, trainIdx_list):
        kp_left_each_data = kp_left[queryIdx].pt
        kp_right_each_data = kp_right[trainIdx].pt
        vector_x = kp_right_each_data[0] - kp_left_each_data[0]
        vector_y = kp_right_each_data[1] - kp_left_each_data[1]
        vector_x_list.append(kp_right_each_data[0] - kp_left_each_data[0])
        vector_y_list.append(kp_right_each_data[1] - kp_left_each_data[1])

    avg_vector_x = sum(vector_x_list) / len(vector_x_list)
    avg_vector_y = sum(vector_y_list) / len(vector_y_list)
    print(avg_vector_x, avg_vector_y)

    int_avg_vector_x = int(avg_vector_x)
    int_avg_vector_y = int(avg_vector_y)
    print(int_avg_vector_x, int_avg_vector_y)

    return [int_avg_vector_x, int_avg_vector_y]
