import cv2
import numpy as np
import os
import shutil

def calc_similarity(img1_path, img2_path):
    print("adgb")
    img1 = cv2.imdecode(np.fromfile(img1_path, dtype=np.uint8), -1)
    H1 = cv2.calcHist([img1], [1], None, [256], [0, 256])  # 计算图直方图
    H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)  # 对图片进行归一化处理
    img2 = cv2.imdecode(np.fromfile(img2_path, dtype=np.uint8), -1)
    H2 = cv2.calcHist([img2], [1], None, [256], [0, 256])  # 计算图直方图
    H2 = cv2.normalize(H2, H2, 0, 1, cv2.NORM_MINMAX, -1)  # 对图片进行归一化处理
    similarity1 = cv2.compareHist(H1, H2, 0)  # 相似度比较
    print('similarity:', similarity1)
    if similarity1 > 0.98:  # 0.98是阈值，可根据需求调整
        return True
    else:
        return False


import os
#from imagededup.methods import PHash

# def process_file(img_path):
#     """
#     处理图片去重
#     :return:
#     """
#     try:
#         phasher = PHash()  # WHash、AHash
#         # 生成图像目录中所有图像的二值hash编码
#         encodings = phasher.encode_images(image_dir=img_path)
#         # print(encodings)
#         # 对已编码图像寻找重复图像
#         duplicates = phasher.find_duplicates(encoding_map=encodings)
#         print(duplicates)
#         only_img = []  # 唯一图片
#         like_img = []  # 相似图片
#
#         for img, img_list in duplicates.items():
#             if img not in only_img and img not in like_img:
#                 only_img.append(img)
#                 like_img.extend(img_list)
#
#         # 删除文件
#         for like in like_img:
#             print("like:  ", like)
#             like_src = os.path.join(img_path, like)
#             if os.path.exists(like_src):
#                 os.remove(like_src)
#
#     except Exception as e:
#         print(e)


def get_image_filenames(folder_path):
    # 初始化一个空列表，用于存储图片的文件名（不含扩展名）
    image_filenames = []

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否是图片（这里假设图片文件有常见的图片扩展名）
        if filename.lower().endswith(('.jpg')):
            # 分割文件名和扩展名
            name, _ = os.path.splitext(filename)
            # 将文件名（不含扩展名）添加到列表中
            image_filenames.append(name)

    return image_filenames

def delete_txt_files_not_in_list(folder_path, file_list):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.txt'):
            # 检查文件名是否不在列表中
            if filename not in file_list:
                # 构造完整的文件路径
                file_path = os.path.join(folder_path, filename)
                # 删除文件
                os.remove(file_path)
                print(f"Deleted: {filename}")



if __name__ == "__main__":
    # img_path = r"F:\yolov5-master\dataset\VOC2012\valid\images"
    # process_file(img_path)
    folder_path = r"F:\yolov5-master\dataset\brainwash\val\labels"
    folder_path1 = r"F:\yolov5-master\dataset\brainwash\val\images"
    # # 调用函数并打印结果
    image_list = get_image_filenames(folder_path1)
    #print(image_list)
    txt_filenames = [filename + '.txt' for filename in image_list]
    print(txt_filenames)
    # #print(len(txt_filenames))
    delete_txt_files_not_in_list(folder_path, txt_filenames)

