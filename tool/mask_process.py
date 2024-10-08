import cv2
from sklearn.cluster import KMeans
from tool.read_directory_files import get_basename
from util.constants import *

def get_max_mask(image_path, lower, upper):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_mask = cv2.inRange(hsv_image, lower, upper)
    # 尋找連通區域
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(color_mask)
    largest_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1  # 跳過背景
    # 創建一個只包含最大連通區域的遮罩
    largest_component_mask = np.zeros_like(color_mask)
    largest_component_mask[labels == largest_label] = 255
    # ---
    return largest_component_mask


def get_max_mask_area(image_path, lower, upper):
    largest_component_mask = get_max_mask(image_path, lower, upper)

    # 忽略黑色背景，只計算白色像素點
    # todo 輸出圖檔後的 countNonZero(cv2.readimg(mask.jpg)) 與 直接計算的 countNonZero(largest_component_mask) 值不相同
    # countNonZero(cv2.readimg(mask.jpg)) 較大 countNonZero(largest_component_mask) 較小
    # cv2.imwrite(f"output/testOuO/tomato_mask/mask_{get_basename(image_path)}", largest_component_mask)
    # temp_img = cv2.imread(f"output/testOuO/tomato_mask/mask_{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    # ---
    cv2.imwrite("output/temp/temp_img.jpg", largest_component_mask)
    temp_img = cv2.imread("output/temp/temp_img.jpg", cv2.IMREAD_GRAYSCALE)
    white_area = cv2.countNonZero(temp_img)
    # ---
    return white_area


def get_color_mask_area(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # --- get G
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    # cv2.imwrite(f"output/testOuO/green_mask/{get_basename(image_path)}", green_mask)
    # tempG_img = cv2.imread(f"output/testOuO/green_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f"output/temp/tempG.jpg", green_mask)
    tempG_img = cv2.imread(f"output/temp/tempG.jpg", cv2.IMREAD_GRAYSCALE)
    # --- get R
    green_and_red_mask = cv2.inRange(hsv_image, lower_GR, upper_GR)
    # cv2.imwrite(f"output/testOuO/GR_mask/{get_basename(image_path)}", green_and_red_mask)
    # tempGR_img = cv2.imread(f"output/testOuO/GR_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f"output/temp/tempGR.jpg", green_and_red_mask)
    tempGR_img = cv2.imread(f"output/temp/tempGR.jpg", cv2.IMREAD_GRAYSCALE)
    R_image = cv2.bitwise_and(tempGR_img, cv2.bitwise_not(tempG_img))
    # cv2.imwrite(f"output/testOuO/red_mask/{get_basename(image_path)}", R_image)
    # tempR_img = cv2.imread(f"output/testOuO/red_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f"output/temp/tempR.jpg", R_image)
    tempR_img = cv2.imread(f"output/temp/tempR.jpg", cv2.IMREAD_GRAYSCALE)
    """
    # --- get tomato
    tomato_mask = get_max_mask(hsv_image, lower_background, upper_background)
    cv2.imwrite(f"output/testOuO/tomato_mask/{get_basename(image_path)}", tomato_mask)
    tomato_image = cv2.imread(f"output/testOuO/tomato_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    # --- get B
    B_image = cv2.bitwise_and(tomato_image, cv2.bitwise_not(tempGR_img))
    cv2.imwrite(f"output/testOuO/brown_mask/{get_basename(image_path)}", B_image)
    tempB_img = cv2.imread(f"output/testOuO/brown_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    """
    # ---
    total_mask_area = get_max_mask_area(image_path, lower_background, upper_background)
    green_area = cv2.countNonZero(tempG_img)
    red_area = cv2.countNonZero(tempR_img)
    brown_area = total_mask_area - green_area - red_area
    return [total_mask_area, red_area, green_area, brown_area]


def get_color_mask_area_and_mask_image(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # --- get G
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    cv2.imwrite(f"output/testOuO/green_mask/{get_basename(image_path)}", green_mask)
    tempG_img = cv2.imread(f"output/testOuO/green_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    # --- get R
    green_and_red_mask = cv2.inRange(hsv_image, lower_GR, upper_GR)
    cv2.imwrite(f"output/testOuO/GR_mask/{get_basename(image_path)}", green_and_red_mask)
    tempGR_img = cv2.imread(f"output/testOuO/GR_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    R_image = cv2.bitwise_and(tempGR_img, cv2.bitwise_not(tempG_img))
    cv2.imwrite(f"output/testOuO/red_mask/{get_basename(image_path)}", R_image)
    tempR_img = cv2.imread(f"output/testOuO/red_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    # --- get tomato
    tomato_mask = get_max_mask(image_path, lower_background, upper_background)
    cv2.imwrite(f"output/testOuO/tomato_mask/{get_basename(image_path)}", tomato_mask)
    tomato_image = cv2.imread(f"output/testOuO/tomato_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    # --- get B
    B_image = cv2.bitwise_and(tomato_image, cv2.bitwise_not(tempGR_img))
    cv2.imwrite(f"output/testOuO/brown_mask/{get_basename(image_path)}", B_image)
    # tempB_img = cv2.imread(f"output/testOuO/brown_mask/{get_basename(image_path)}", cv2.IMREAD_GRAYSCALE)
    # ---
    total_mask_area = get_max_mask_area(image_path, lower_background, upper_background)
    green_area = cv2.countNonZero(tempG_img)
    red_area = cv2.countNonZero(tempR_img)
    brown_area = total_mask_area - green_area - red_area
    return [total_mask_area, red_area, green_area, brown_area]


# --- 測試遮罩
# from tool.mask_process import get_color_mask_area_and_mask_image
# from tool.read_directory_files import list_files_in_directory
# for img_name in list_files_in_directory("data_testimage/data_testimage_TPH_Ruifang/"):
#     frame_path = "data_testimage/data_testimage_TPH_Ruifang/" + img_name
#     area = get_color_mask_area_and_mask_image(frame_path)
#     print(area)
# print("done.")


# 利用分群找三色像素點 -> 效果不佳(R、B同色相)
def kMeans_clay_pixel(image_path, mask_path):
    # 讀取番茄照片和遮罩
    tomato_image = cv2.imread(image_path)
    mask_image = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    masked_image = cv2.bitwise_and(tomato_image, tomato_image, mask=mask_image)

    # 將圖像轉換為HSV顏色空間  # print(hsv_image.shape) -> (500, 500, 3)
    hsv_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2HSV)

    # 將圖像轉換為二維陣列以適應K-means  # print(pixels.shape) -> (250000, 3)
    pixels = hsv_image.reshape((-1, 3))
    # 僅對遮罩部分進行分群
    isZero = np.all(pixels == 0, axis=1)
    pixels_not_zero = pixels[~isZero]

    # 使用K-means算法將像素值分為3個集群
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(pixels_not_zero)
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    # 將分群結果(0、1、2)加回遮罩部分
    labels_index = 0
    real_labels_list = []
    for pixel_index in range(len(isZero)):
        pixels_is_zero = isZero[pixel_index]
        if pixels_is_zero:
            pixels_label = 3
        else:
            pixels_label = labels[labels_index]
            labels_index += 1
        real_labels_list.append(pixels_label)

    real_labels = np.asarray(real_labels_list)
    real_centers = np.append(centers, [[0, 0, 0]], axis=0)
    print(real_centers)

    # 重新組合分群結果示意圖
    cluster_image = real_centers[real_labels].reshape(masked_image.shape).astype(np.uint8)
    cv2.imwrite("../output/testOuO/cluster_image.jpg", cluster_image)

    return cluster_image


# --- 測試kMeans分群對色塊分析效果
# kMeans_clay_pixel(image_path="../data_testimage/data_testimage_TPH_Ruifang/0_3_0_C0185_001.jpg", mask_path="../output/testOuO/tomato_mask/0_3_0_C0185_001.jpg")
