import numpy as np

# 定義 Red 的 HSV 範圍
lower_0R_3y = np.array([170, 140, 45])
upper_0R_3y = np.array([180, 220, 155])
lower_0R_4y = np.array([65, 100, 30])
upper_0R_4y = np.array([180, 255, 180])
lower_0R_5y = np.array([170, 105, 40])
upper_0R_5y = np.array([180, 225, 180])
lower_0R_6y = np.array([170, 125, 35])
upper_0R_6y = np.array([180, 225, 225])
lower_0R = [lower_0R_3y, lower_0R_4y, lower_0R_5y, lower_0R_6y]
upper_0R = [upper_0R_3y, upper_0R_4y, upper_0R_5y, upper_0R_6y]
lower_1R_3y = np.array([170, 110, 60])
upper_1R_3y = np.array([180, 225, 165])
lower_1R_4y = np.array([170, 120, 50])
upper_1R_4y = np.array([180, 235, 195])
lower_1R_5y = np.array([170, 85, 75])
upper_1R_5y = np.array([180, 230, 190])
lower_1R_6y = np.array([170, 80, 70])
upper_1R_6y = np.array([180, 220, 190])
lower_1R = [lower_1R_3y, lower_1R_4y, lower_1R_5y, lower_1R_6y]
upper_1R = [upper_1R_3y, upper_1R_4y, upper_1R_5y, upper_1R_6y]

# 定義 Green 的 HSV 範圍
lower_0G_3y = np.array([20, 65, 20])
upper_0G_3y = np.array([75, 200, 155])
lower_0G_4y = np.array([20, 60, 65])
upper_0G_4y = np.array([60, 200, 190])
lower_0G_5y = np.array([30, 105, 40])
upper_0G_5y = np.array([125, 225, 185])
lower_0G_6y = np.array([20, 55, 55])
upper_0G_6y = np.array([65, 185, 190])
lower_0G = [lower_0G_3y, lower_0G_4y, lower_0G_5y, lower_0G_6y]
upper_0G = [upper_0G_3y, upper_0G_4y, upper_0G_5y, upper_0G_6y]
lower_1G_3y = np.array([40, 110, 60])
upper_1G_3y = np.array([65, 225, 165])
lower_1G_4y = np.array([45, 120, 50])
upper_1G_4y = np.array([70, 235, 195])
lower_1G_5y = np.array([40, 85, 75])
upper_1G_5y = np.array([60, 230, 190])
lower_1G_6y = np.array([40, 80, 70])
upper_1G_6y = np.array([65, 220, 190])
lower_1G = [lower_1G_3y, lower_1G_4y, lower_1G_5y, lower_1G_6y]
upper_1G = [upper_1G_3y, upper_1G_4y, upper_1G_5y, upper_1G_6y]

# 定義 Brown 的 HSV 範圍
lower_0B_3y = np.array([0, 40, 20])
upper_0B_3y = np.array([180, 130, 80])
lower_0B_4y = np.array([0, 45, 40])
upper_0B_4y = np.array([180, 90, 105])
lower_0B_5y = np.array([0, 35, 40])
upper_0B_5y = np.array([180, 100, 100])
lower_0B_6y = np.array([0, 40, 40])
upper_0B_6y = np.array([180, 105, 120])
lower_0B = [lower_0B_3y, lower_0B_4y, lower_0B_5y, lower_0B_6y]
upper_0B = [upper_0B_3y, upper_0B_4y, upper_0B_5y, upper_0B_6y]
lower_1B_3y = np.array([0, 0, 45])
upper_1B_3y = np.array([180, 115, 90])
lower_1B_4y = np.array([0, 40, 45])
upper_1B_4y = np.array([180, 130, 90])
lower_1B_5y = np.array([0, 0, 40])
upper_1B_5y = np.array([180, 100, 90])
lower_1B_6y = np.array([0, 0, 0])
upper_1B_6y = np.array([180, 120, 110])
lower_1B = [lower_1B_3y, lower_1B_4y, lower_1B_5y, lower_1B_6y]
upper_1B = [upper_1B_3y, upper_1B_4y, upper_1B_5y, upper_1B_6y]
