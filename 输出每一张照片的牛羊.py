import os
import pandas as pd

# 指定文件夹路径
folder_path = 'C:\\mq\\yolov8\\code\\ultralytics\\runs\\detect\\20231024_five jiaci\\labels'

# 初始化一个空的DataFrame
df = pd.DataFrame(columns=['文件名', '牛', '羊'])

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        # 初始化计数器
        cow_count, sheep_count = 0, 0
        # 读取文件并统计
        with open(file_path, 'r') as file:
            for line in file:
                label = line.split()[0]
                if label == '0':
                    cow_count += 1
                elif label == '1':
                    sheep_count += 1
        # 使用pandas.concat来添加数据
        new_row = pd.DataFrame({'文件名': [filename[:-4]], '牛': [cow_count], '羊': [sheep_count]})
        df = pd.concat([df, new_row], ignore_index=True)


# 指定输出Excel文件的路径
output_excel_path = 'C:\\mq\\yolov8\\code\\ultralytics\\runs\\detect\\20231024_five jiaci\\result.xlsx'
# 保存到Excel文件
df.to_excel(output_excel_path, index=False)
