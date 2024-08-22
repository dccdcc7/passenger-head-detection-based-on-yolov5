import os

# 指定文件夹路径
folder_path = './dataset/VOC2012/valid/images'

# 用于重命名的起始编号
start_number = 1

# 遍历文件夹中的所有文件
for filename in sorted(os.listdir(folder_path)):
    # 检查文件扩展名是否为.jpg
    if filename.lower().endswith('.jpg'):
        # 构建完整的文件路径
        old_file_path = os.path.join(folder_path, filename)

        # 构建新的文件名，使用起始编号
        new_filename = f"{start_number}.jpg"  # 使用3位数的编号，不足的前面补0
        new_file_path = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"文件 {filename} 已重命名为 {new_filename}")

        # 更新起始编号
        start_number += 1

        # 如果已经重命名了200个文件，就停止
        if start_number > 200:
            break

# for i in range(128):
#     img_folder_path ='./dataset/VOC2012/valid/labels'
#     img_path = img_folder_path+ f"/{i+1}.jpg"
#     print(img_path)