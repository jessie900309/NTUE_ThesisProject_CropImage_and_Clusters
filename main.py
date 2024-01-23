
# 擷取影片中間 20s(constants) 作為使用資料，並且每 4frame(constants) 另存為圖片
# 呼叫函數，將影片中間20秒的 frame 每隔4個 frame 存成圖片檔
# input: video_dir / output: output_dir
# ---
# print("run get_video_frames()")
# from tool.get_video_frame import get_video_frames
# from tool.read_directory_files import list_files_in_directory, check_and_create_directory
# from util.constants import video_duration, video_frame_interval
# video_dir = 'data_video'
# output_dir = 'output/frames'
# check_and_create_directory(output_dir)
# for video_name in list_files_in_directory(video_dir):
#     video_path = video_dir + '/' + video_name
#     output_frame_dir = f'{output_dir}/{video_name[:-4]}'
#     check_and_create_directory(output_frame_dir)
#     get_video_frames(video_path=video_path, output_folder=output_frame_dir, duration=video_duration, frame_interval=video_frame_interval)
# print("done.")


# 擷取圖片中間 500x500 另存為圖片
# input: frame_dir / output: output_dir
# ---
# print("run image_crop_square()")
# from tool.image_crop import image_crop_square
# from tool.read_directory_files import list_dirs_in_directory, list_files_in_directory, check_and_create_directory, get_basename
# from util.constants import square_width
# all_frame_dir = 'output/frames'
# for dir_name in list_dirs_in_directory(all_frame_dir):
#     frame_dir = all_frame_dir + '/' + dir_name
#     output_dir = f'output/frames_500x500/{get_basename(frame_dir)}'
#     check_and_create_directory(output_dir)
#     for frame_name in list_files_in_directory(frame_dir):
#         frame_path = frame_dir + '/' + frame_name
#         output_cropped_path = f'{output_dir}/{frame_name[:-4]}_cropped_500x500.jpg'
#         image_crop_square(image_path=frame_path, output_path=output_cropped_path, pixel=square_width)
#         loop_count = (list_files_in_directory(frame_dir)).index(frame_name)
#         if loop_count % 10 == 0:
#             print(f"正在輸出第{loop_count}張frame: {output_cropped_path}")
# print("done.")


# 修正500x500位置
# R. right -> +x  L. left <- -x
# D. down   v +y  U. up    ^ -y
# ---
# print("run image_crop_square() EDIT!!!")
# from tool.image_crop import image_crop_square_edit
# from tool.read_directory_files import list_files_in_directory, check_and_create_directory, get_basename
# from util.constants import square_width
# edit_vid_name = '1_6_0_C0207'
# frame_dir = 'output/frames/' + edit_vid_name
# output_dir = f'output/frames_500x500/{get_basename(frame_dir)}'
# check_and_create_directory(output_dir)
# for frame_name in list_files_in_directory(frame_dir):
#     frame_path = frame_dir + '/' + frame_name
#     output_cropped_path = f'{output_dir}/{frame_name[:-4]}_cropped_500x500.jpg'
#     image_crop_square_edit(image_path=frame_path, output_path=output_cropped_path, pixel=square_width)
#     loop_count = (list_files_in_directory(frame_dir)).index(frame_name)
#     if loop_count % 10 == 0:
#         print(f"正在輸出第{loop_count}張frame: {output_cropped_path}")
# print("done.")


# 取得影像遮罩
# ---
# from tool.image_draw_HSVmask import get_HSVcolor_mask
# from tool.read_directory_files import list_files_in_directory, check_and_create_directory
# from util.HSV_threshold import *
# set_color = 'brown'
# input_dir = 'output/frames_500x500/0_3_0_C0144/'
# output_dir = 'output/color_mask_only/0_3_0_C0144/'+set_color
# check_and_create_directory(output_dir)
# for img_name in list_files_in_directory(input_dir):
#     loop_count = (list_files_in_directory(input_dir)).index(img_name)
#     if loop_count % 50 == 0:
#         print(f"正在輸出第{loop_count}張影像")
#     img_path = input_dir + img_name
#     get_HSVcolor_mask(image_path=img_path, lower=lower_brown[0], upper=upper_brown[0], output_folder=output_dir)
# print("done.")


# 尋找最大連通區域的遮罩
# ---
# from tool.mask_process import find_max_area
# from tool.read_directory_files import list_files_in_directory, check_and_create_directory
# input_dir = 'output/color_mask_only/1_6_0_C0096/red/'
# output_dir = 'output/color_mask_only/1_6_0_C0096/red_max_area/'
# check_and_create_directory(output_dir)
# for img_name in list_files_in_directory(input_dir):
#     loop_count = (list_files_in_directory(input_dir)).index(img_name) + 1
#     if loop_count % 100 == 0:
#         print(f"正在輸出第{loop_count}張影像")
#     img_path = input_dir + img_name
#     find_max_area(mask_path=img_path, output_folder=output_dir)
# print("done.")


# 計算遮罩的像素數(面積)
# ---
# from tool.mask_process import calculate_white_area
# from tool.read_directory_files import list_files_in_directory
# import csv
# for video_name in ['0_3_0_C0144', '0_4_0_C0125', '0_5_0_C0104', '1_6_0_C0096']:
#     input_dir = f'output/color_mask_only/{video_name}/'
#     output_path = f'output/final_chart_redmax/{video_name}_mask_area.csv'
#     no = 0
#     with open(output_path, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['no', 'red', 'green', 'brown', 'total'])
#         for img_name in list_files_in_directory(input_dir+'red_max_area/'):
#             no += 1
#             red_mask_area = calculate_white_area(input_dir + 'red_max_area/' + img_name)
#             green_mask_area = calculate_white_area(input_dir + 'green/' + img_name)
#             brown_mask_area = calculate_white_area(input_dir + 'brown/' + img_name)
#             total = red_mask_area + green_mask_area + brown_mask_area
#             writer.writerow([no, red_mask_area, green_mask_area, brown_mask_area, total])
#             if no % 100 == 0:
#                 print(f"正在計算{video_name}的第{no}張影像")
# print("done.")


# 資料視覺化，三色面積
# ---
# from tool.get_final_chart import get_final_chart
# csv_folder = 'output/final_chart_redmax/'
# csv_list = ['0_3_0_C0144_mask_area.csv', '0_4_0_C0125_mask_area.csv', '0_5_0_C0104_mask_area.csv', '1_6_0_C0096_mask_area.csv']
# for csv in csv_list:
#     csv_path = csv_folder + csv
#     get_final_chart(csv_path=csv_path, output_folder=csv_folder)
# print("done.")

