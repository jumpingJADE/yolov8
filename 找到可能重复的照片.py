import pandas as pd
import shutil
import os

# 替换为你的Excel文件路径
excel_file_path = 'C:\\mq\\yolov8\\code\\ultralytics\\runs\\detect\\20231024_five jiaci\\niu.xlsx'
# Excel中照片名列的列名，假设是第一列，通常列名可以在Excel文件的第一行找到
photo_column_name = '文件名'
# 替换为你的照片所在的文件夹路径
photos_folder_path = 'C:\\mq\\yolov8\\code\\ultralytics\\runs\\detect\\20231024_five jiaci\\images'
# 替换为你想要复制照片到的目标路径
destination_folder_path = 'C:\\Users\\Apexmo\\OneDrive\\Desktop\\photo\\dupulicate'

# 读取Excel文件
df = pd.read_excel(excel_file_path)
print("从Excel文件中读取的照片名：", df[photo_column_name].tolist())

# 确保目标文件夹存在
if not os.path.exists(destination_folder_path):
    os.makedirs(destination_folder_path)

# 遍历文件夹中的照片
for photo in os.listdir(photos_folder_path):
    photo_name_without_extension, _ = os.path.splitext(photo)  # 去掉扩展名
    print("正在检查照片：", photo_name_without_extension)
    if photo_name_without_extension in df[photo_column_name].values:
        original_photo_path = os.path.join(photos_folder_path, photo)
        destination_photo_path = os.path.join(destination_folder_path, photo)
        shutil.copy2(original_photo_path, destination_photo_path)
        print(f"复制照片：{photo} -> {destination_photo_path}")

print("处理完成。")