import cv2
from tool.read_directory_files import get_basename


def get_video_frames(video_path, output_folder, duration=10, frame_interval=10):
    # 取得檔案名稱(不包含路徑、副檔名)
    file_name = get_basename(video_path)[:-4]

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("無法開啟影片")
        return

    # 獲取影片的 FPS (frames per second) 以及總幀數
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 計算擷取的起點和結束點
    start_frame = int((total_frames - fps * duration) / 2)
    end_frame = int((total_frames + fps * duration) / 2) + frame_interval

    # 設定計數器來命名保存的圖片檔
    frame_count = 0
    output_frame_count = 0

    # 循環遍歷每一個 frame
    while True:
        ret, frame = cap.read()
        if not ret or frame_count > end_frame:
            break

        # 只擷取指定時間範圍的 frame，並以指定間隔取樣
        if (start_frame <= frame_count) and (frame_count <= end_frame) and (frame_count % frame_interval == 0):
            output_file_path = f'{output_folder}/{file_name}_frame_{frame_count:05d}.jpg'
            cv2.imwrite(output_file_path, frame)
            output_frame_count += 1
            if output_frame_count % 50 == 0:
                print(f"正在輸出第{output_frame_count:03d}張frame: {output_file_path}")

        frame_count += 1
        if output_frame_count >= 600:
            break

    # 釋放資源
    cap.release()
