import pandas as pd

# 假设您的Excel文件路径为 'your_excel_file.xlsx'
excel_path = 'your_excel_file.xlsx'

# 读取Excel文件
df = pd.read_excel(excel_path)

# 提取前缀并创建新列
df['前缀'] = df['文件名'].apply(lambda x: x.split('_')[0])

# 对牛羊数量进行分组汇总
grouped = df.groupby('前缀').sum()

# 重置索引，将前缀作为一列
grouped.reset_index(inplace=True)

# 更改列名以符合您的要求
grouped.columns = ['文件名', '牛', '羊']

# 输出到新的Excel文件
output_path = 'summarized_data.xlsx'
grouped.to_excel(output_path, index=False)

print(f'汇总数据已经保存到 "{output_path}"。')
