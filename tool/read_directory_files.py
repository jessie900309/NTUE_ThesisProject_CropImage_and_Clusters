import os.path


def list_dirs_in_directory(directory_path):
    dirs = os.listdir(directory_path)
    # dir only
    dirs = [dir for dir in dirs if os.path.isdir(os.path.join(directory_path, dir))]
    return dirs


def list_files_in_directory(directory_path):
    files = os.listdir(directory_path)
    # file only
    files = [file for file in files if os.path.isfile(os.path.join(directory_path, file))]
    return files


def check_and_create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"創建資料夾: {directory_path}")
    else:
        print(f"資料夾存在: {directory_path}")


def get_basename(file_path):
    return os.path.basename(file_path)
