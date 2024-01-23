import os
import csv
from util.constants import school_name, data_column


def get_ddata(dir_path, output_path):
    all_file_name = os.listdir(dir_path)
    no = 0
    # txt to csv
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data_column)
        for txt_name in all_file_name:
            print("read file : {}".format(txt_name))
            txt_path = dir_path + '/' + txt_name
            school = school_name[txt_name]
            with open(txt_path) as f:
                for line in f:
                    mp4_file_name = line.rstrip()
                    data = line.split("_")
                    sex = data[0]
                    age = data[1]
                    stu = data[2]
                    mp4_file_name = mp4_file_name + ".MP4"
                    no += 1
                    writer.writerow([no, sex, age, stu, school, mp4_file_name])
