import os

def count_lines_in_folder(folder_path):
    count_cattle = 0
    count_sheep = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith("0"):
                            count_cattle += 1
                        elif line.startswith("1"):
                            count_sheep += 1
    return count_cattle, count_sheep

# 指定文件夹的路径
folder_path = r"C:\mq\yolov8\code\ultralytics\runs\detect\20231020_one jiaci\labels"

# 调用函数计算每行首字符为0和首字符为1的总数
count_cattle, count_sheep = count_lines_in_folder(folder_path)

print(f"文件夹 {folder_path} 及其子文件夹中所有txt文件中牛的总数为: {count_cattle}")
print(f"文件夹 {folder_path} 及其子文件夹中所有txt文件中羊的总数为: {count_sheep}")