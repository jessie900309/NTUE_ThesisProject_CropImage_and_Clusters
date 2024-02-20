
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


# 取得影像遮罩並計算最大連通區域的像素數(面積)
# ---
import csv
from tool.mask_process import get_max_mask_area
from tool.read_directory_files import list_dirs_in_directory, list_files_in_directory, get_basename
from util.constants import upper_red, lower_red, upper_green, lower_green, upper_brown, lower_brown
input_dir = 'output/frames_500x500_O/0_3_0_C0185/'

for frame_img in list_dirs_in_directory(input_dir):
    video_name = get_basename(input_dir)
    output_path = f'output/{video_name}_mask_area.csv'
    no = 0
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['no', 'red', 'green', 'brown', 'total'])
        for img_name in list_files_in_directory(input_dir+'red/'):
            no += 1
            red_mask_area = get_max_mask_area(frame_img, upper=upper_red, lower=lower_red)
            green_mask_area = get_max_mask_area(frame_img, upper=upper_green, lower=lower_green)
            brown_mask_area = get_max_mask_area(frame_img, upper=upper_brown, lower=lower_brown)
            total = red_mask_area + green_mask_area + brown_mask_area
            writer.writerow([no, red_mask_area, green_mask_area, brown_mask_area, total])
            if no % 100 == 0:
                print(f"正在計算{video_name}的第{no}張影像")
print("done.")
