import torch
import torch.nn as nn

class Simple3LayerConv(nn.Module):
    def __init__(self, in_channels=3, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(in_channels, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1)
        )
        self.classifier = nn.Linear(64, num_classes)

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        return self.classifier(x)

def test_model():
    """用來確保模型能跑的測試小函數"""
    model = Simple3LayerConv()
    x = torch.randn(1, 3, 32, 32)
    print(f"✅ 模型建立成功！輸出維度: {model(x).shape}")