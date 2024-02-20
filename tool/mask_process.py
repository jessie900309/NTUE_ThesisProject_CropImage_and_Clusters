import cv2
import numpy as np


def get_max_mask_area(image_path, lower, upper):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_mask = cv2.inRange(hsv_image, lower, upper)
    # 尋找連通區域
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(color_mask)
    largest_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1  # 跳過背景
    # 創建一個只包含最大連通區域的遮罩
    largest_component_mask = np.zeros_like(color_mask)
    largest_component_mask[labels == largest_label] = 255
    # 忽略黑色背景，只計算白色像素點 result_image = cv2.bitwise_and(color_mask, color_mask, mask=largest_component_mask)
    # todo 輸出圖檔後的 countNonZero(cv2.readimg(mask.jpg)) 與 直接計算的 countNonZero(largest_component_mask) 值不相同
    # countNonZero(cv2.readimg(mask.jpg)) 較大 countNonZero(largest_component_mask) 較小
    cv2.imwrite("../temp_img.jpg", largest_component_mask)
    temp_img = cv2.imread("../temp_img.jpg", cv2.IMREAD_GRAYSCALE)
    white_area = cv2.countNonZero(temp_img)

    return white_area

