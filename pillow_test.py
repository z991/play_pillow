from PIL import Image
#  读取文件
im = Image.open("boat_girl_small_p.png")
#  打印图片的格式，图片的大小， 图片的模式
print(im.format, im.size, im.mode)
#  获取图片的长宽
w, h = im.size

print('boat_girl image size: %sx%s' % (w, h))
"""
thumbnail: 把这个图像做成一个缩略图。此方法修改
包含自身的缩略图版本，不大于
给定的大小。此方法计算适当的缩略图
保持图像的大小
"""
im.thumbnail((w//2, h//2))

im.save('boat_girl_small_p.png', 'jpeg')

from PIL import Image
from random import randint
import os
import time
#  判断这个文件夹是否存在，不存在新创建
if os.path.exists('newpic'):
  pass
else:
    os.mkdir('newpic')
for i in range(1, 10):
    # new 创建具有给定模式和大小的新图像。
    im = Image.new('RGB', (200, 200), (randint(0,255), randint(0,255), randint(0,255)))
    time.sleep(0.2)
    im.save('./newpic/'+str(i)+'.png')