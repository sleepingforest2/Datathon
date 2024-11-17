import numpy as np
import pandas as pd

# 假设你有一个 CSV 文件路径和一个包含索引的 .npy 文件路径
csv_file = 'D:\datathon/FI_score.csv'  # 输入的 CSV 文件路径
npy_file = 'D:\datathon/indices2.npy'  # 存储行索引的 .npy 文件路径
output_csv_file = 'D:\datathon/output_FI.csv'  # 输出的 CSV 文件路径

# 读取 .npy 文件，得到索引
indices = np.load(npy_file)

# 读取 CSV 文件
df = pd.read_csv(csv_file)

# 使用索引选择对应的行
selected_rows = df.iloc[indices]

# 去掉 'icd_codes' 列中的所有 '#' 字符
# selected_rows['icd_codes'] = selected_rows['icd_codes'].str.replace('#', '', regex=False)

# 将选择的行保存到新的 CSV 文件
selected_rows.to_csv(output_csv_file, index=False)

print(f"选中的行已保存到 '{output_csv_file}'，并去除了 'icd_codes' 列中的 '#' 字符。")