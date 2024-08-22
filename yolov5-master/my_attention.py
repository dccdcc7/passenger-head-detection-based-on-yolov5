import torch
import torch.nn as nn
import torch.nn.functional as F

import torch
import torchvision
import torchvision.transforms as transforms

# 定义图像预处理操作
# transform = transforms.Compose([
#     transforms.RandomHorizontalFlip(),
#     transforms.RandomCrop(32, padding=4),
#     transforms.ToTensor(),
#     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
# ])
# # 下载并加载CIFAR-10训练集
# trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
# batch_size = 4
# train_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# classes = ('plane', 'car', 'bird', 'cat',
#            'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

class SpatialMultiScaleAttention(nn.Module):
    def __init__(self, in_channels, num_scales):
        super(SpatialMultiScaleAttention, self).__init__()
        self.in_channels = in_channels
        self.num_scales = num_scales

        # Define the attention layers
        self.attention_layers = nn.ModuleList()
        for _ in range(num_scales):
            self.attention_layers.append(nn.Conv2d(in_channels, 1, kernel_size=1, stride=1, padding=0))

    def forward(self, x):
        # x: input tensor of shape (batch_size, in_channels, height, width)
        batch_size, _, height, width = x.size()

        # Calculate attention maps for each scale
        attention_maps = []
        for i in range(self.num_scales):
            attention_map = self.attention_layers[i](x)
            attention_map = F.softmax(attention_map.view(batch_size, -1), dim=1)
            attention_map = attention_map.view(batch_size, 1, height, width)
            #print(attention_map.size())
            #attention_map = attention_map.expand(1, self.in_channels, height, width)
            attention_maps.append(attention_map)


        # Concatenate attention maps
        attention_maps = torch.cat(attention_maps, dim=1)
        attention_maps.expand(batch_size, self.in_channels, height, width)
        print(x.size())
        print(attention_maps.size())
        # Apply attention to the input
        x = x * attention_maps
        return x

class MultiScaleAttentionCNN(nn.Module):
    def __init__(self, in_channels, num_classes, num_scales):
        super(MultiScaleAttentionCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, 64, kernel_size=3, stride=1, padding=1)
        self.attention1 = SpatialMultiScaleAttention(64, num_scales)
        self.attention1 = SpatialMultiScaleAttention(64, 64)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.fc = nn.Linear(128, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.attention1(x)
        x = F.relu(self.conv2(x))
        x = F.adaptive_avg_pool2d(x, (1, 1))
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

class CNN(nn.Module):
    def __init__(self, in_channels, num_classes, num_scales):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, 64, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.fc = nn.Linear(128, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.adaptive_avg_pool2d(x, (1, 1))
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x


# Train the model
if __name__ == "__main__":
    input = torch.rand(16, 3, 64, 64)
    #print(input)
    #print(input.shape)
    model = MultiScaleAttentionCNN(3,10,3)
    #model = CNN(in_channels=3, num_classes=10, num_scales=3)
    output = model(input)
    print(output.shape)
