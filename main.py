
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
# for vid_name in list_dirs_in_directory(all_frame_dir):
#     frame_dir = all_frame_dir + '/' + vid_name
#     output_dir = f'output/frames_500x500/{get_basename(frame_dir)}'
#     check_and_create_directory(output_dir)
#     for frame_name in list_files_in_directory(frame_dir):
#         loop_count = (list_files_in_directory(frame_dir)).index(frame_name)
#         frame_path = frame_dir + '/' + frame_name
#         output_cropped_path = f'{output_dir}/{vid_name}_{loop_count+1:03d}.jpg'
#         image_crop_square(image_path=frame_path, output_path=output_cropped_path, pixel=square_width)
#         if loop_count % 10 == 0:
#             print(f"正在輸出第{loop_count}張frame: {output_cropped_path}")
# print("done.")


# 修正區塊位置
# R. right -> +x  L. left <- -x
# D. down   v +y  U. up    ^ -y
# ---
# print("run image_crop_square() EDIT!!!")
# from tool.image_crop import image_crop_square_edit
# from tool.read_directory_files import list_files_in_directory, check_and_create_directory, get_basename
# edit_vid_name = '0_4_0_C0067'
# frame_dir = 'output/frames/' + edit_vid_name
# output_dir = f'output/frames_500x500/{get_basename(frame_dir)}'
# check_and_create_directory(output_dir)
# for frame_name in list_files_in_directory(frame_dir):
#     loop_count = (list_files_in_directory(frame_dir)).index(frame_name)
#     frame_path = frame_dir + '/' + frame_name
#     output_cropped_path = f'{output_dir}/{edit_vid_name}_{loop_count+1:03d}.jpg'
#     image_crop_square_edit(image_path=frame_path, output_path=output_cropped_path)
#     if loop_count % 10 == 0:
#         print(f"正在輸出第{loop_count}張frame: {output_cropped_path}")
# print("done.")


# 取得三色黏土遮罩像素數(面積)
# ---
# import csv
# from tool.mask_process import get_color_mask_area
# from tool.read_directory_files import list_dirs_in_directory, list_files_in_directory
# input_dir = 'datasets/frames_500x500/'
#
# for video_name in list_dirs_in_directory(input_dir):
#     output_path = f'output/frames_row_data/{video_name}_mask_area.csv'
#     no = 0
#     with open(output_path, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['no', 'total_mask_area', 'red_mask_area', 'green_mask_area', 'brown_mask_area'])
#         for img_name in list_files_in_directory(input_dir+video_name):
#             no += 1
#             frame_img = input_dir+video_name + '/' + img_name
#             row_data = get_color_mask_area(frame_img)
#             row_data.insert(0, no)
#             # print(row_data, "T：", type(row_data))
#             writer.writerow(row_data)
#             if no % 100 == 0:
#                 print(f"正在計算{video_name}的第{no}張影像")
# print("done.")


# 統計數值資料
# import csv
# from tool.get_Ddata import read_csv
# from tool.read_directory_files import list_files_in_directory
# input_dir = "datasets/frames_row_data/"
# output_path = "output/output.csv"
# with open(output_path, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['sex', 'age', 'stu', 'school', 'video_name',
#                      'total_avg', 'total_std', 'total_var', 'total_max', 'total_min', 'total_q25', 'total_q50', 'total_q75',
#                      'red_avg', 'red_std', 'red_var', 'red_max', 'red_min', 'red_q25', 'red_q50', 'red_q75',
#                      'green_avg', 'green_std', 'green_var', 'green_max', 'green_min', 'green_q25', 'green_q50', 'green_q75',
#                      'brown_avg', 'brown_std', 'brown_var', 'brown_max', 'brown_min', 'brown_q25', 'brown_q50', 'brown_q75'])
#     for csv_file in list_files_in_directory(input_dir):
#         student_info = csv_file.split("_")
#         sex = student_info[0]
#         age = student_info[1]
#         stu = student_info[2]
#         video_name = csv_file[:-14]
#         row_data = [sex, age, stu, "TPH_Ruifang", video_name]
#         csv_path = input_dir + csv_file
#         clay_info = read_csv(csv_path)
#         for info in clay_info:
#             row_data.append(info)
#         writer.writerow(row_data)
