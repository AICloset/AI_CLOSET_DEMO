import torch
import torchvision.models as models
import torch.nn as nn
from PIL import Image
import torchvision
from torchvision import datasets, models, transforms
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def imshow(input, title):
    # torch.Tensor를 numpy 객체로 변환
    input = input.numpy().transpose((1, 2, 0))
    # 이미지 정규화 해제하기
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    input = std * input + mean
    input = np.clip(input, 0, 1)
    # 이미지 출력
    plt.imshow(input)
    plt.title(title)
    plt.show()

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = models.resnet34()
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 3)  # make the change
model.load_state_dict(torch.load('C:\\ai_closet_demo\\pattern_recognize\\model_weights.pth', map_location=device))
model.to(device)

transforms_test = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    # transforms.CenterCrop(120)
])


image = Image.open('C:\\ai_closet_demo\\image\\adidas.PNG')
image = transforms_test(image).unsqueeze(0).to(device)

class_names = ['checked pattern', 'flower pattern', 'stripe pattern']

with torch.no_grad():
    outputs = model(image) # 모델에 이미지 넣기
    _, preds = torch.max(outputs, 1)
    imshow(image.cpu().data[0], title='Predict : ' + class_names[preds[0]])