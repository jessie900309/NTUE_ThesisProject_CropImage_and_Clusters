import cv2
from tool.read_directory_files import get_basename


def draw_HSVcolor_mask(image_path, lower, upper, output_folder):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_image, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    output_path = output_folder + "/" + "_mask_" + get_basename(image_path)
    cv2.imwrite(output_path, result)


def get_HSVcolor_mask(image_path, lower, upper, output_folder):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_image, lower, upper)

    output_path = output_folder + "/" + "mask_" + get_basename(image_path)
    cv2.imwrite(output_path, mask)


# 測試色彩閾值
# from tool.image_draw_HSVmask import draw_HSVcolor_mask, get_HSVcolor_mask
# from tool.read_directory_files import list_files_in_directory
# from util.constants import upper_background, lower_background
# for test_img in list_files_in_directory('data_testimage/'):
#     frame_img = 'data_testimage/' + test_img
#     print(frame_img)
#     draw_HSVcolor_mask(frame_img, upper=upper_background, lower=lower_background, output_folder='output/testOuO')
#     get_HSVcolor_mask(frame_img, upper=upper_background, lower=lower_background, output_folder='output/testOuO')
