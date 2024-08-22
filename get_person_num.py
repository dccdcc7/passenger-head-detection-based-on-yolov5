import os
from detect import parse_opt
from detect import main
from onnx11 import onnx_forward
# 指定文件夹路径
list_gt = []
list_pre = []
list_pre_onnx=[]
list_folder_gt = []
folder_path = './dataset/VOC2012/test/labels/'  # 替换为你的文件夹路径
# 获取文件夹中的所有文件和文件夹名称
# entries = os.listdir(folder_path)
# # 打印文件和文件夹名称
# for entry in entries:
#     list_folder_gt.append(entry)
#
#
def count_lines_large_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for i, _ in enumerate(file):
            pass
    return i + 1  # 因为enumerate从0开始计数，所以需要+1
#
# # 使用函数
# for item in list_folder_gt:
#     item = folder_path+item
#     number_of_lines = count_lines_large_file(item)
#     list_gt.append(number_of_lines)
#
# print(list_gt)

# for item in list_gt:
#     print(f"The large file has {item} lines.")

print('------------------------------------------------------------------------------')
def run():

    total_precision=0
    total_num=0
    for i in range(48):
        img_folder_path ='./dataset/VOC2012/test/images'
        txt_folder_path = './dataset/VOC2012/test/labels'
        # if i==1 or i==122 or i==91 or i==84 or i==68 or i==32 or i==111 or  i==113:
        #     continue
        img_path = img_folder_path+ f"/{i+1}.jpg"
        if os.path.exists(img_path):
            i=i*1
        else:
            i+=1
        #print(img_path)
        img_path = img_folder_path + f"/{i+1}.jpg"
        opt = parse_opt(img_path)
        number = main(opt)
        #print(number)
        txt_path = txt_folder_path+f"/{i+1}.txt"
        gt_number = count_lines_large_file(txt_path)
        print("gt:",gt_number,"pre_num:",number)
        precision = float(1 - (abs(gt_number - number) / gt_number))
        print(img_path," : ",precision)
        total_precision = total_precision + precision
        total_num=total_num+1
    print(total_precision/total_num)
#list_pre_onnx = onnx_forward()

#print(list_pre.length())
# for item in list_pre:
#     print(f"The large file has {item} lines.")
# print(list_pre)
#
# total_precision = 0
# for item1, item2 ,item3 in zip(list_gt, list_pre, list_folder_gt):
#     print(item1, item2)
#     precision = float(1-(abs(item1-item2)/item1))
#     print(item3," : ",precision)
#     total_precision = total_precision + precision
# print("total precison is ",total_precision/len(list_pre))
run()