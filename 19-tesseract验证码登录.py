# 安装Tesseract-ORC.exe,配置系统环境变量Path
# 使用命令：tesseract tupian.png abc
# Tesseract-ORC还可自行训练库，增强识别准确率

import pytesseract
from PIL import Image

# 识别率不高（免费）
img = Image.open('yzm.png')
code = pytesseract.image_to_string(img)
print(code)