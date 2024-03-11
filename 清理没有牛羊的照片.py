import os
import shutil

# 定义label和images文件夹的路径
label_dir = 'C:\\mq\\yolov8\\code\\ultralytics\\runs\\detect\\20231024_five jiaci\\labels'
images_dir = 'C:\\mq\\yolov8\\code\\ultralytics\\runs\detect\\20231024_five jiaci\\images'

# 获取label文件夹中所有文件的文件名（不包含扩展名）
labels = [os.path.splitext(file)[0] for file in os.listdir(label_dir) if file.endswith('.txt')]

# 遍历images文件夹中的所有图片文件
for img_file in os.listdir(images_dir):
    if img_file.endswith('.jpg'):
        # 检查图片文件名（不包含扩展名）是否在labels列表中
        img_name = os.path.splitext(img_file)[0]
        if img_name not in labels:
            # 如果不在列表中，则删除该图片
            img_path = os.path.join(images_dir, img_file)
            print(f"Deleting {img_path}")  # 打印将要删除的文件名
            os.remove(img_path)  # 删除文件

print("完成图片清理。")
