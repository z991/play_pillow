from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母:
def rndChar():
    # chr  ASCII控制字符
    return chr(random.randint(65, 90))
# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
"""
truetype : 从文件或类似文件的对象加载TrueType或OpenType字体，
并创建一个字体对象。
此函数从给定文件或类似文件加载字体对象
对象，并为给定大小的字体创建字体对象。
"""
font = ImageFont.FreeTypeFont('SFNSRounded.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)

image.save('code_sfnss.jpg', 'jpeg')