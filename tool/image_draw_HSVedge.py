import cv2


def draw_HSVcolor_edge(image_path, lower, upper, output_path):

    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv_image, lower, upper)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    result_image = image.copy()
    cv2.drawContours(result_image, contours, -1, (0, 0, 255), 2)

    cv2.imwrite(output_path, result_image)


# main()：在圖上框出紅色區域(棄用)
# ---
# print("run find_red_contours()")
# from tool.image_draw_HSVedge import draw_red_edge
# from tool.read_directory_files import list_files_in_directory, check_and_create_directory, get_basename
# frame_dir = 'output/frames_500x500/test_video'
# output_dir = f'output/frames_red_edge/{get_basename(frame_dir)}'
# check_and_create_directory(output_dir)
# for frame_name in list_files_in_directory(frame_dir):
#     frame_path = frame_dir + '/' + frame_name
#     output_edge_path = f'{output_dir}/{frame_name[:-4]}_red.jpg'
#     draw_red_edge(image_path=frame_path, output_path=output_edge_path)
#     loop_count = (list_files_in_directory(frame_dir)).index(frame_name)
#     if loop_count % 10 == 0:
#         print(f"正在輸出第{loop_count}張frame: {output_edge_path}")
# print("done.")

