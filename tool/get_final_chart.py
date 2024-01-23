import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tool.read_directory_files import get_basename

color_list = {'red': 'r', 'green': 'g', 'brown': 'saddlebrown', 'total': 'lightgrey'}

def get_final_chart(csv_path, output_folder):
    df = pd.read_csv(csv_path)
    for column_name in ['red', 'green', 'brown', 'total']:
        line_length_list = df[column_name].values
        angles = np.arange(0, 360, 0.6)
        # chart
        plt.figure(figsize=(8, 8))
        for i in range(600):
            line_length = line_length_list[i]
            angles_rad = np.radians(angles[i])
            x = line_length * np.cos(angles_rad)
            y = line_length * np.sin(angles_rad)
            # plt.plot(x, y, 'ro', markersize=5)
            plt.plot([0, x], [0, y], color=color_list[column_name])
        plt.title('Radiating Lines')
        plt.xlim(-70000, 70000)
        plt.ylim(-70000, 70000)
        plt.hlines(y=0, xmin=-70000, xmax=70000, colors=['black'])
        plt.vlines(x=0, ymin=-70000, ymax=70000, colors=['black'])
        csv_name = get_basename(csv_path)
        print(f"正在輸出：{output_folder}{csv_name[:-4]}_{column_name}.jpg")
        plt.savefig(f"{output_folder}{csv_name[:-4]}_{column_name}.jpg")
