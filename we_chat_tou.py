import os
import math

from wxpy import Bot
from PIL import Image


# 创建头像存放文件夹
def creat_filepath():
    #  返回一个表示当前工作目录的unicode字符串。
    """
    /Users/zhuxuanyu/python_xuexi/pil_play
    :return:
    """
    avatar_dir = os.getcwd() + "/wechat/"
    if not os.path.exists(avatar_dir):
        os.mkdir(avatar_dir)
    return avatar_dir


# 保存好友头像
def save_avatar(avatar_dir):
    # 初始化机器人，扫码登陆
    bot = Bot()
    friends = bot.friends(update=True)
    num = 0
    for friend in friends:
        friend.get_avatar(avatar_dir + '/' + str(num) + ".jpg")
        num = num + 1


# 拼接头像
def joint_avatar(path):
    # 设置画布大小(正方形)
    image_size = 2560
    # 获取文件夹内头像个数
    length = len(os.listdir(path))
    """
    计算所需各行列的头像数量
    """
    # sqrt 开平方
    x_lines = math.ceil(math.sqrt(length))  # 图片x 轴放多少个好友头像
    y_lines = math.ceil(math.sqrt(length))  # 图片y 轴放多少个好友头像
    # 设置每个头像大小       拼接后图片长度 / x(y)轴 好友头像的个数
    each_size = math.ceil(image_size / math.floor(math.sqrt(length)))

    image = Image.new('RGB', (each_size * x_lines, each_size * y_lines))
    x = 0  # x 轴索引值
    y = 0  # y 轴索引值
    for (root, dirs, files) in os.walk(path):
        for pic_name in files:
            # 增加头像读取不出来的异常处理
            try:
                with Image.open(path + pic_name) as img:
                    """
                    resize(self, size, resample=NEAREST, box=None):
                    返回此图像的大小调整后的副本。
                    """
                    img = img.resize((each_size, each_size))
                    """
                    paste(self, im, box=None, mask=None):
                    将另一个图像粘贴到此图像中。box参数要么是
                    一个2元组给出左上角，一个4元组定义
                    左，上，右，和低像素坐标，或没有(相同的
                    (0,0))。看到裁判:“坐标系”。如果给定了一个4元组，则给出其大小
                    所粘贴图像的大小必须与所粘贴区域的大小相匹配。
                    """
                    image.paste(img, (x * each_size, y * each_size))
                    x += 1
                    if x == x_lines:
                        x = 0
                        y += 1
            except IOError:
                print("头像读取失败")

    img = image.save(os.getcwd() + "/wechat.png")
    print('微信好友头像拼接完成!')


if __name__ == '__main__':
    avatar_dir = creat_filepath()
    save_avatar(avatar_dir)
    joint_avatar(avatar_dir)
    # for (root, dirs, files) in os.walk(avatar_dir):
    #     print(root, dirs, files)

