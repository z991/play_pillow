import os
import math
from PIL import Image


# 拼接头像
def joint_avatar(path):
    # 获取文件夹内头像个数
    length = len(os.listdir(path))
    # 设置画布大小
    image_size = 2560
    # 设置每个头像大小
    each_size = math.ceil(image_size / math.floor(math.sqrt(length)))
    # 计算所需各行列的头像数量
    x_lines = math.ceil(math.sqrt(length))
    y_lines = math.ceil(math.sqrt(length))
    image = Image.new('RGB', (each_size * x_lines, each_size * y_lines))
    x = 0
    y = 0
    for (root, dirs, files) in os.walk(path):
        for pic_name in files:
            # 增加头像读取不出来的异常处理
            try:
                with Image.open(path + pic_name) as img:
                    img = img.resize((each_size, each_size))
                    image.paste(img, (x * each_size, y * each_size))
                    x += 1
                    if x == x_lines:
                        x = 0
                        y += 1
            except IOError:
                print("头像读取失败")

    img = image.save(os.getcwd() + "/wechat.png")
    print('微信好友头像拼接完成!')

def join_boat_girl():

    boat_girl = Image.open("boat_girl.jpg")
    w, h = boat_girl.size
    #
    # boat_girl.thumbnail((w // 2, h // 2))
    #
    # boat_girl.save('boat_girl_small_2.jpg', 'jpeg')
    x_lines = y_lines = 2
    

    image = Image.new('RGB', (w, h))
    x = 0
    y = 0
    for i in range(4):
        # 增加头像读取不出来的异常处理
        try:
            each_size_x = int(w / 2) + 1
            each_size_y = int(h / 2) + 1
            img = boat_girl.resize((each_size_x+1, each_size_y))
            image.paste(img, (x * each_size_x, y * each_size_y))
            x += 1
            if x == x_lines:
                x = 0
                y += 1
        except IOError:
            print("头像读取失败")
    img = image.save(os.getcwd() + "/boat_girl_4_q.png")


if __name__ == '__main__':
    # save_avatar(avatar_dir)
    # joint_avatar(avatar_dir)
    join_boat_girl()
    pass