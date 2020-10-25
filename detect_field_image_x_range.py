import cv2


def detect_field_image_x_range(detect_field_image_file_path):
    color_image = cv2.imread(detect_field_image_file_path)
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    bw_image = cv2.threshold(gray_image, 254, 255, cv2.THRESH_BINARY)[1]

    x_left_end_point = 0
    x_right_end_point = color_image.shape[1]
    y_top_end_point = 0
    y_bottom_end_point = color_image.shape[0]

    x_min = None
    x_max = None
    size = None

    contours = cv2.findContours(
        bw_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    vertex_cordinate_list = []
    for index in range(0, len(contours)):
        vertex_cordinate_data = cv2.boundingRect(contours[index])
        x_left = vertex_cordinate_data[0]
        y_top = vertex_cordinate_data[1]
        x_right = x_left + vertex_cordinate_data[2]
        y_bottom = y_top + vertex_cordinate_data[3]
        vertex_cordinate = {
            "x_left": x_left,
            "y_top": y_top,
            "x_right": x_right,
            "y_bottom": y_bottom
        }
        vertex_cordinate_list.append(vertex_cordinate)
        if x_left == x_left_end_point and y_top == y_top_end_point and y_bottom == y_bottom_end_point:
            x_min = vertex_cordinate["x_right"] + 1
        if x_right == x_right_end_point and y_bottom == y_bottom_end_point and y_top == y_top_end_point:
            x_max = vertex_cordinate["x_left"] - 1

    if (x_max - x_min + 1) % 2 == 0:
        size = abs(int((x_max - x_min + 1) / 2))
    elif (x_max - x_min + 1) % 2 == 1:
        size = abs(int((x_max - x_min) / 2))
    else:
        size = None

    left_image_x_min = None
    left_image_x_max = None
    left_image_y_top = y_top_end_point
    left_image_y_bottom = y_bottom_end_point
    right_image_x_min = None
    right_image_x_max = None
    right_image_y_top = y_top_end_point
    right_image_y_bottom = y_bottom_end_point

    if size is not None:
        left_image_x_min = x_min
        left_image_x_max = x_min + size - 1
        right_image_x_max = x_max
        right_image_x_min = x_max - size + 1

    field_image_x_range = [
        left_image_x_min,
        left_image_x_max,
        left_image_y_top,
        left_image_y_bottom,
        right_image_x_min,
        right_image_x_max,
        right_image_y_top,
        right_image_y_bottom,
        left_image_x_max - left_image_x_min,
        right_image_x_max - right_image_x_min
    ]
    print(field_image_x_range)
    return field_image_x_range
