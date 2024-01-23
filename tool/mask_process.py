import cv2
import numpy as np
from tool.read_directory_files import get_basename


def erode_and_erosion(mask_path, kernel_x, iteration, output_folder):
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    # kernel：rectangle
    # kernel = np.ones((kernel_x, kernel_x), np.uint8)
    # kernel：circle
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_x, kernel_x))
    # 侵蝕再膨脹
    erosion = cv2.erode(mask, kernel, iterations=iteration)
    dilation = cv2.dilate(erosion, kernel, iterations=iteration)

    output_path = output_folder + f"processed_{iteration}_{kernel_x}x{kernel_x}" + get_basename(mask_path)
    cv2.imwrite(output_path, dilation)


# main()：對遮罩侵蝕再膨脹(棄用)
# ---
# from tool.mask_process import erode_and_erosion
# from tool.read_directory_files import list_files_in_directory, check_and_create_directory
# input_dir = 'output/test_color_mask_only/red/'
# output_dir = 'output/test_mask_processed/circle/'
# check_and_create_directory(output_dir)
# for img_name in list_files_in_directory(input_dir):
#     loop_count = (list_files_in_directory(input_dir)).index(img_name)
#     print(f"正在輸出第{loop_count}張影像")
#     img_path = input_dir + img_name
#     print(img_path)
#     erode_and_erosion(mask_path=img_path, kernel_x=5, iteration=2, output_folder=output_dir)
# print("done.")


def find_max_area(mask_path, output_folder):
    image = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # 二值化，將影像轉為黑白
    _, binary_mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    # 尋找連通區域
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_mask)
    # 找到最大的連通區域的索引
    largest_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1  # 跳過背景
    # 創建一個只包含最大連通區域的遮罩
    largest_component_mask = np.zeros_like(binary_mask)
    largest_component_mask[labels == largest_label] = 255
    # 忽略黑色背景，只計算白色像素點
    result_image = cv2.bitwise_and(image, image, mask=largest_component_mask)

    new_mask_path = output_folder + get_basename(mask_path)
    cv2.imwrite(new_mask_path, result_image)


def calculate_white_area(mask_path):
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    white_area = cv2.countNonZero(mask)
    return white_area

