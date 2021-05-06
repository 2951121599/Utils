# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  均值滤波.py
# 当前系统日期时间：2020/7/21，15:50 
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


# 均值滤波
def blur(source):
    """
    注：

    1）随着核大小逐渐变大，会让图像变得更加模糊；

    2）如果设置为核大小为（1，1），则结果就是原始图像。

    :param source:
    :return:
    """
    img = cv2.blur(source, (3, 3))  # result = cv2.blur(原始图像,核大小)

    cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cv2img)

    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    draw.text((0, 0), "均值滤波", (255, 0, 0), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体

    # PIL图片转cv2 图片
    cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    cv2.imshow("blur", cv2charimg)


# 中值滤波
def medianBlur(source):
    img = cv2.medianBlur(source, 3)
    cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cv2img)

    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    draw.text((0, 0), "中值滤波", (255, 0, 0), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
    # PIL图片转cv2 图片
    cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    cv2.imshow("medianBlur", cv2charimg)


# 方框滤波
def BoxFilter(source):
    img = cv2.boxFilter(source, -1, (5, 5), normalize=1)
    cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cv2img)

    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    draw.text((0, 0), "方框滤波", (255, 0, 0), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
    # PIL图片转cv2 图片
    cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    cv2.imshow("boxFilter", cv2charimg)


# 高斯滤波
def GaussianBlur(source):
    img = cv2.GaussianBlur(source, (3, 3), 0)
    cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cv2img)

    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    draw.text((0, 0), "高斯滤波", (255, 0, 0), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
    # PIL图片转cv2 图片
    cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    cv2.imshow("GaussianBlur", cv2charimg)


# 高斯边缘检测
def Gaussian(source):
    sobelX = cv2.Sobel(source, cv2.CV_64F, 1, 0)  # x方向的梯度
    sobelY = cv2.Sobel(source, cv2.CV_64F, 0, 1)  # y方向的梯度

    sobelX = np.uint8(np.absolute(sobelX))  # x方向梯度的绝对值
    sobelY = np.uint8(np.absolute(sobelY))  # y方向梯度的绝对值

    img = cv2.bitwise_or(sobelX, sobelY)  #
    cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cv2img)

    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    draw.text((0, 0), "高斯边缘检测", "green", font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体

    # PIL图片转cv2 图片
    cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    cv2.imshow("GaussianBlur", cv2charimg)


if __name__ == "__main__":
    # 加载图片
    img = cv2.imread("./ml_data/test2.png")
    cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input image", img)
    blur(img)
    medianBlur(img)
    GaussianBlur(img)
    # Gaussian(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
