
"""
數據資料
"""

# 數據資料欄位

data_column = ['no', 'sex', 'age', 'stu', 'school', 'file_name']

# 各檔案統計之對應學校代號
school_name = {
    "2023_1020_count51.txt": "TPH_Tamsui",
    "2023_1027_count14.txt": "TPH_Ruifang",
    "2023_1031_count25.txt": "TYC_Dongmen",
    "2023_1101_count19.txt": "TYC_Dongmen",
    "2023_1102_count21.txt": "TYC_Dongmen",
    "2023_1103_count22.txt": "TYC_Dongmen",
    "2023_1110_count13.txt": "TPH_Ruifang",
    "2023_1124_count16.txt": "TPH_Ruifang",
    "2023_1222_count13.txt": "TPH_Ruifang"
}

"""
影像資料
"""

# 影片擷取區間
video_duration = 20  # 秒(s)
video_frame_interval = 4  # 幀(frame)

# 圖片擷取邊長
square_width = 500


import numpy as np

# 定義作品背景閾值
lower_background = np.array([0, 40, 10])
upper_background = np.array([180, 220, 185])

