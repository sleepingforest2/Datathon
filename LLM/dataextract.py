import csv
import re

import pandas as pd
import string
import numpy as np

# 所有字符集
characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + '#'+'.')

# 假设我们将它们编码到 8x8 的二维矩阵中
rows = 8
cols = 8

# 编码：将字符映射到二维坐标
char_to_coord = {}
for idx, char in enumerate(characters):
    row = idx // cols
    col = idx % cols
    char_to_coord[char] = (row, col)


# 定义转换字符串到嵌入向量的函数
def string_to_embedding(input_string):
    embedding = []
    # 将字符串中的每个字符转换为对应的二维坐标，并保留为二维向量
    for char in input_string:
        if char in char_to_coord:
            row, col = char_to_coord[char]
            embedding.append([row, col])  # 将每个字符的坐标作为一个二维向量

    def normalize_embedding(embedding):
        # 计算所有二维向量的最小值和最大值
        min_val = min(min(row) for row in embedding)  # 获取最小值
        max_val = max(max(row) for row in embedding)  # 获取最大值

        # 如果最大值和最小值相等，表示所有值相同，无法归一化
        if max_val == min_val:
            return [[0.5, 0.5]] * len(embedding)  # 所有值相同的情况下，将其归一化为中间值

        # 归一化每个二维向量中的值到 [0, 1] 范围
        normalized_embedding = [
            [(value - min_val) / (max_val - min_val) for value in row] for row in embedding
        ]
        return normalized_embedding

    return normalize_embedding(embedding)

df_vector = pd.read_csv('data.csv')  # 显示前 10 行数据
print(df_vector.head(10))
# 用于存储所有行的列表
rows_list = df_vector.values.tolist()

# 匹配
B = pd.read_csv('FI_score.csv')

# 确保 'hadm_id' 存在
id = np.array([row[0] for row in rows_list])  # 将 'hadm_id' 列提取为 NumPy 数组

# 确保 B['hadm_id'] 是一个 NumPy 数组
hadm_id_B = np.array(B['hadm_id'])
Y = np.array(B['FI_score'])

# 使用 np.isin() 筛选出 id 中存在于 B['hadm_id'] 中的元素
filtered_id = id[np.isin(id, hadm_id_B)]

# 获取这些元素在 A 中的索引
indices = np.where(np.isin(id, filtered_id))[0]
indices2 = np.where(np.isin(hadm_id_B, filtered_id))[0]

# 按照索引筛选行
row = [rows_list[i] for i in indices2]
Y = [Y[i] for i in indices2]
np.save('D:\datathon/Y.npy', Y)
np.save('D:\datathon/indices.npy', indices)
np.save('D:\datathon/indices2.npy', indices2)
np.save('D:\datathon/filtered_id.npy', filtered_id)
# 去掉每一行的第一列
rows_list_filtered = [r[1:] for r in row]
c = [str(row) for row in rows_list_filtered]
max_length = max(len(s) for s in c)
c_cleaned = [re.sub(r"[;\[\]',]", "", s) for s in c]
# 对每个字符串进行处理，若长度小于 max_length，则在末尾补充 #
c_padded = [s + '#' * (max_length - len(s)) if len(s) < max_length else s for s in c_cleaned]
# 将每一行转换为字符串
rows_str = [string_to_embedding(row) for row in c_padded]

max_length = 11
Y = [str(s) + '0' * (max_length - len(str(s))) if len(str(s)) < max_length else str(s)for s in Y]
Y_matrix = [string_to_embedding(row) for row in Y]
matrix = np.array(rows_str)
Y_embbed = np.array(Y_matrix)
# 输出结果的形状
print(matrix.shape)  # 应该输出 (2000, 251, 2)
# 假设 padded_rows_str 是包含 NumPy 数组的列表
np.save('padded_rows_str.npy', matrix)
np.save('Y_embbed.npy', Y_embbed)