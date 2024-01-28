import numpy as np

# 定義 Red 的 HSV 範圍
lower_red_3y = np.array([170, 114, 45])
upper_red_3y = np.array([180, 218, 112])
lower_red_4y = np.array([150, 90, 5])
upper_red_4y = np.array([180, 255, 145])
lower_red_5y = np.array([170, 80, 30])
upper_red_5y = np.array([180, 230, 135])
lower_red_6y = np.array([170, 80, 30])
upper_red_6y = np.array([180, 230, 135])
lower_red = [lower_red_3y, lower_red_4y, lower_red_5y, lower_red_6y]
upper_red = [upper_red_3y, upper_red_4y, upper_red_5y, upper_red_6y]

# 定義 Green 的 HSV 範圍
lower_green_3y = np.array([30, 60, 15])
upper_green_3y = np.array([70, 235, 135])
lower_green_4y = np.array([50, 60, 10])
upper_green_4y = np.array([90, 255, 140])
lower_green_5y = np.array([40, 60, 55])
upper_green_5y = np.array([70, 225, 125])
lower_green_6y = np.array([50, 60, 25])
upper_green_6y = np.array([70, 255, 120])
lower_green = [lower_green_3y, lower_green_4y, lower_green_5y, lower_green_6y]
upper_green = [upper_green_3y, upper_green_4y, upper_green_5y, upper_green_6y]

# 定義 Brown 的 HSV 範圍
lower_brown_3y = np.array([0, 40, 0])
upper_brown_3y = np.array([180, 85, 65])
lower_brown_4y = np.array([125, 15, 0])
upper_brown_4y = np.array([160, 155, 85])
lower_brown_5y = np.array([0, 45, 0])
upper_brown_5y = np.array([25, 145, 85])
lower_brown_6y = np.array([0, 50, 0])
upper_brown_6y = np.array([180, 180, 80])
lower_brown = [lower_brown_3y, lower_brown_4y, lower_brown_5y, lower_brown_6y]
upper_brown = [upper_brown_3y, upper_brown_4y, upper_brown_5y, upper_brown_6y]

