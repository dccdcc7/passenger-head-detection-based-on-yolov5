我们了解了一种新的卷积架构，也就是空间和通道重构卷积。并根据次提出了我们的特征提取架构C2f_S，其能够处理图像的空间和通道信息，改善了原本卷积对于图像的色彩和空间分析时不够细致和高效的问题，同时。我们将yolov5中的C3层中的bottleneck替换成了由空间和通道重构卷积所搭建的Bottleneck_ScConv，并为了减少网络参数和提高特征学习能力，我们将yolov5中的C3层按照yolov8的思想进行了优化。使得其在减少参数量的同时，能够更好地提取特征。
 
   
左图为我们改进后的检测结果，中图为gt，右图为yolov5原始网络的检测结果
由此可见模型对于图像特征的提取能力得到了增强，能够更好地针对小目标检测
争对之前训练遇到的过拟合问题，我们检查了数据集，发现数据集中很多图像的相似度非常的高，这是因为很多图像都是在视频切帧得来的，因此相似度非常的高。因此采用基于图像hash值的比较方法进行数据清洗，并重新制作了验证集和测试集。再次训练发现过拟合情况有所缓解。
1、项目：智慧座舱，模型的改进已经取得了显著的提升、下一步直接与yolov8进行比较，并进行一系列消融实验。同时用于验证模型性能的验证集的质量不是特别好，要进行重新制作，并划分为三种。第一种是easy的数据集，其中人脸或后脑勺相对清晰、存在一定的遮挡情况（这种情况与实际情况比较相符），第二种是由一段长视频切帧得到的图像，使用这样的数据进行验证能够更好地反映模型的鲁棒性和模型的检测速率，第三种是hard的数据集，这个数据集中存在较多的遮挡情况，且人脸或者后脑勺相对模糊。同时我们在这个数据集上进行了数据增强，即对图像进行翻转，添加高斯噪声，降低曝光或亮度等措施，能够更好地反映模型的鲁棒性。

Method 	Dataset	Task	Map50	Map75	Gflops	FPS
Yolov5	Easy	detect	0.884	0.522	15.8	36.7
	Hard	detect	0.694	0.283	15.8	36.3
	Continous	detect	0.808	0.456	15.8	36.4
Yolov8	Easy	detect				
	Hard	detect				
	Continous	detect				
Yolov5+retina-facev5	Easy	detect				
	Hard	detect				
	Continous	detect				
ours	Easy	detect	0.903	0.576	15.0	37.4
	Hard	detect	0.74	0.298	15.0	37.4
	Continous	detect	0.873	0.487	15.0	37.4
检测实例展示，左侧为yolov5 baseline，右侧为ours
人物运动导致信息丢失的情况下：
  
小目标+大尺度差异
  
遮挡情况下
  
在验证集上进行自定评价指标的测试：
Method 	Dataset	Task	Our Metric
Yolov5	Easy	detect	0.898
	Hard	detect	0.602
	Continous	detect	0.832
Yolov8	Easy	detect	
	Hard	detect	
	Continous	detect	
Yolov5+retina-facev5	Easy	detect	
	Hard	detect	
	Continous	detect	
ours	Easy	detect	0.952
	Hard	detect	0.667
	Continous	detect	0.918
