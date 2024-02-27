import cv2


def image_crop_square(image_path, output_path, pixel):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # 定義擷取區域
    top_left_x = int((width - pixel) / 2)
    top_left_y = height - pixel - 80
    bottom_right_x = top_left_x + pixel
    bottom_right_y = height - 80

    # 擷取指定區域
    cropped_image = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

    # 保存擷取的區域影像
    cv2.imwrite(output_path, cropped_image)



def image_crop_square_edit(image_path, output_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # 定義擷取區域
    top_left_x = int((width - 500) / 2) + 40
    top_left_y = height - 500 - 80
    bottom_right_x = top_left_x + 500
    bottom_right_y = height - 80
    # print('top_left_x : ', top_left_x)
    # print('top_left_y : ', top_left_y)
    # print('bottom_right_x : ', bottom_right_x)
    # print('bottom_right_y : ', bottom_right_y)

    # 擷取指定區域
    cropped_image = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

    # 保存擷取的區域影像
    cv2.imwrite(output_path, cropped_image)
