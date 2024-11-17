import csv
import json
import csv

# # 读取 CSV 文件并按比例拆分数据
# input_file = 'D:\datathon/output.csv'  # 输入的原始 CSV 文件路径
# train_file = 'D:\datathon/data_train_half_new.csv'  # 训练集 CSV 文件路径
# test_file = 'D:\datathon/data_test_half_new.csv'  # 测试集 CSV 文件路径

# # 读取原始数据
# with open(input_file, newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     header = next(reader)  # 获取表头
#     data = list(reader)  # 读取所有数据行
#
# num_rows = len(data)
# # 计算训练集和测试集的分割点
# train_size = int(num_rows * 0.9)  # 90% 的数据作为训练集
#
# # 划分数据
# train_data = data[:train_size]  # 训练集数据
# test_data = data[train_size:]   # 测试集数据
#
# # 将训练集数据写入新的 CSV 文件
# with open(train_file, mode='w', newline='', encoding='utf-8') as train_csvfile:
#     writer = csv.writer(train_csvfile)
#     writer.writerow(header)  # 写入表头
#     writer.writerows(train_data)  # 写入训练集数据
#
# # 将测试集数据写入新的 CSV 文件
# with open(test_file, mode='w', newline='', encoding='utf-8') as test_csvfile:
#     writer = csv.writer(test_csvfile)
#     writer.writerow(header)  # 写入表头
#     writer.writerows(test_data)  # 写入测试集数据

paraA = "icd_codes"
paraB = "drg_code"
paraC = "drg_severity"
paraD = "drg_mortality"

all_templates = []

with open('D:/datathon/data_test_half_new.csv', newline='', encoding='utf-8') as csvfile1, open('D:/datathon/data_test_half_y_new.csv', newline='', encoding='utf-8') as csvfile2:
    reader1 = csv.DictReader(csvfile1)
    reader2 = csv.DictReader(csvfile2)

    for row1, row2 in zip(reader1, reader2):
        icd_codes_cleaned = row1[paraA].replace('#', '')  # 去掉 icd_codes 中的 # 字符
        template_base = {
            "instruction": f"icd_codes：{icd_codes_cleaned}, drg_code：{row1[paraB]}, drg_severity：{row1[paraC]}，drg_mortality：{row1[paraD]}",
            "input": "",
            "output": f"{row2['FI_score']}"
        }
        all_templates.append(template_base)

with open('testtemplates_half_new.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(all_templates, jsonfile, ensure_ascii=False, indent=2)

print("JSON数据已成功保存到 'test_templates.json' 文件中")