import torch
from PIL import Image
import numpy as np
from pathlib import Path
import sys,os
from utils.general import check_img_size, scale_boxes, non_max_suppression, xyxy2xywh, strip_optimizer, set_logging
from utils.torch_utils import select_device
import cv2
from models.common import DetectMultiBackend
# 设置日志记录
set_logging()

weights= "./runs/train/exp49/weights/best.pt"  # model path or triton URL
source= "data/images"  # file/dir/URL/glob/screen/0(webcam)
data= "data/VOC1.yaml"  # dataset.yaml path
imgsz=(640, 640)  # inference size (height, width)
conf_thres=0.25  # confidence threshold
iou_thres=0.45  # NMS IOU threshold
max_det=1000  # maximum detections per image
device = select_device("cuda:0") # cuda device, i.e. 0 or 0,1,2,3 or cpu
view_img=False  # show results
save_txt=False  # save results to *.txt
save_csv=False  # save results in CSV format
save_conf=False  # save confidences in --save-txt labels
save_crop=False  # save cropped prediction boxes
nosave=False  # do not save images/videos
classes=None  # filter by class: --class 0, or --class 0 2 3
agnostic_nms=False  # class-agnostic NMS
augment=False  # augmented inference
visualize=False  # visualize features
update=False  # update all models
project="runs/detect"  # save results to project/name
name="exp"  # save results to project/name
exist_ok=False  # existing project/name ok, do not increment
line_thickness=3  # bounding box thickness (pixels)
hide_labels=False  # hide labels
hide_conf=False  # hide confidences
half=False  # use FP16 half-precision inference
dnn=False  # use OpenCV DNN for ONNX inference
vid_stride=1  # video frame-rate stride


# 加载模型

model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data, fp16=half)


# 加载图像
img_path = './data/images/zidane.jpg'  # 图像路径
img0 = Image.open(img_path)  # 打开图像
img = img0.convert('RGB')  # 转换为RGB
img = img.resize((640, 640), Image.BICUBIC)  # 调整图像大小

# 转换图像为模型输入格式
img = torch.from_numpy(np.array(img)).float() / 255.0
img = img.permute(2, 0, 1).unsqueeze(0)  # 转换为CHW格式并增加批次维度
img = img.to('cuda')
# 进行检测
with torch.no_grad():
    pred = model(img, augment=True)[0]

# 后处理
pred = non_max_suppression(pred, 0.4, 0.5, classes=None, agnostic=False)  # NMS
if len(pred) > 0:
    det = pred[0]
    # 将边界框坐标从 xyxy 格式转换为 xywh 格式
    det[:, :4] = scale_boxes(img.shape[2:], det[:, :4], img0.size).round()

# 将PIL图像转换为OpenCV格式的图像
img = np.array(img0)  # PIL图像转换为numpy数组
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # 转换颜色空间

# 使用OpenCV绘制边界框和标签
for *xyxy, conf, cls in reversed(det):
    label = f'{"person"}'
    # OpenCV的坐标格式是 (x, y), 所以需要调整
    x1, y1, x2, y2 = xyxy
    # OpenCV的坐标格式需要两个点：左上角和右下角
    pt1 = (int(x1)/640, int(y1)/640)  # 左上角
    pt2 = (int(x2)/640, int(y2)/640)  # 右下角
    # 绘制边界框
    cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)  # 绿色边界框
    # 绘制标签
    cv2.putText(img, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # 显示图像
cv2.imshow('Detections', img)
cv2.imwrite('output.jpg',img)
cv2.waitKey(0)  # 按任意键关闭窗口


# 保存或显示图像
# ...

