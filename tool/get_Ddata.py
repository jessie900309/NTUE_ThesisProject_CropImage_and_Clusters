import csv
import numpy as np


def read_csv(csv_path):
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # 讀取標頭
        data = np.array([row for row in reader])
    row_data = []
    for i, column in enumerate(header):
        if i == 0:
            continue
        column_data_str = data[:, i]
        column_data = column_data_str.astype(int)
        # ---
        average = np.average(column_data) # 平均數
        std_deviation = np.std(column_data) # 標準差
        variance = np.var(column_data) # 變異數
        max_value = np.max(column_data) # 最大值
        min_value = np.min(column_data) # 最小值
        quartiles = np.percentile(column_data, [25, 50, 75]) # 第一四分位數、中位數、第三四分位數
        # ---
        color_data = [round(average, 4), round(std_deviation, 4), round(variance, 4),
                      max_value, min_value, quartiles[0], quartiles[1], quartiles[2]]
        for value in color_data:
            row_data.append(value)
    return row_data
