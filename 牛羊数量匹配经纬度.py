import pandas as pd

# 读取第一个Excel文件
df1 = pd.read_excel('路径/文件名1.xlsx', engine='openpyxl')

# 读取第二个Excel文件
df2 = pd.read_excel('路径/文件名2.xlsx', engine='openpyxl')

# 根据照片名合并两个DataFrame
merged_df = pd.merge(df1, df2, left_on='照片名', right_on='文件名')

# 删除重复的照片名列（如果你的两个表的第一列名称不同，这一步是必要的）
merged_df.drop('文件名', axis=1, inplace=True)

# 将合并后的DataFrame输出到新的Excel文件
merged_df.to_excel('路径/合并后的文件名.xlsx', index=False, engine='openpyxl')
