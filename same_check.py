# import os
#
# # 指定要检查的文件夹路径
# folder_path = './dataset/brainwash/brainwash_10_27_2014_images'
#
# # 获取文件夹中所有文件的列表
# files = os.listdir(folder_path)
#
# # 提取文件名（不包括后缀），并存储在字典中
# file_names = {}
# duplicates = []
#
# # 遍历文件列表
# for file in files:
#     # 获取不带扩展名的文件名
#     base_name = os.path.splitext(file)[0]
#
#     # 检查文件名是否已在字典中
#     if base_name in file_names:
#         # 如果是，记录为重复文件
#         duplicates.append(base_name)
#     else:
#         # 否则，将文件名添加到字典中
#         file_names[base_name] = file
#
# # 输出结果
# if duplicates:
#     print("存在重名文件（不考虑后缀）:")
#     for dup in duplicates:
#         print(f"重复的文件名: {dup}")
# else:
#     print("文件夹中没有重名文件。")

import os

# 指定要处理的文件夹路径
folder_path = './dataset/brainwash/brainwash_11_24_2014_images'

# 指定要保存新文件的文件夹路径（可以与原文件夹相同）
output_folder = './dataset/brainwash/brainwash_11_24_2014_images1'

# 检查输出文件夹是否存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否是PNG格式
    if filename.lower().endswith('.png'):
        # 获取不带扩展名的文件名
        base_name = os.path.splitext(filename)[0]

        # 构建新的文件名（将后缀改为.jpg）
        new_filename = f"{base_name}.jpg"

        # 构建原始文件的完整路径和新文件的完整路径
        original_file = os.path.join(folder_path, filename)
        new_file = os.path.join(output_folder, new_filename)

        # 复制并重命名文件
        os.rename(original_file, new_file)
        print(f"文件 {filename} 已重命名为 {new_filename}")