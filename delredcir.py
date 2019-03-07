# -*-coding:utf-8-*-
# https://blog.csdn.net/guiyiqixin/article/details/79342531
# 2019/03/07 by sjt

import numpy as np
import cv2


def access_pixels1(img, OutputFile, loop_num=1, loop_max = 2):
    """遍历图像每个像素的每个通道"""
    print(img.shape)              #打印图像的高，宽，通道数（返回一个3元素的tuple）
    height = img.shape[0]        #将tuple中的元素取出，赋值给height，width，channels
    width = img.shape[1]
    channels = img.shape[2]
    print("height:%s,width:%s,channels:%s" % (height,width,channels))
    print(img.size)              #打印图像数组内总的元素数目（总数=高X宽X通道数）

    range_app = 12

    for row in range(height):    #遍历每一行
        for col in range(width): #遍历每一列
            if col - range_app < 0 or row - range_app < 0 or col + range_app > 1919 or row + range_app > 1079:
                continue
            else:
                VB = int(img[row][col][0])
                VG = int(img[row][col][1])
                VR = int(img[row][col][2])
                if (VR > 180 and VB <70 and VG < 70) or ( (VR - VB) >50 and (VR - VG) > 50 ):
                    pixel_sum = []
                    for i_mean in range(1,range_app + 1):               # 求其上下左右各8个的像素的均值
                        for j_mean in range(1,range_app + 1):
                            pixel_sum.append(img[row - j_mean][col - i_mean])
                            pixel_sum.append(img[row - i_mean][col - j_mean])
                            pixel_sum.append(img[row + j_mean][col + i_mean])
                            pixel_sum.append(img[row + i_mean][col - j_mean])
                    try:
                        sum_len = len(pixel_sum)
                        VB_N = [x[0] for x in pixel_sum]
                        VB_N = sum(VB_N) / sum_len
                        VG_N = [x[1] for x in pixel_sum]
                        VG_N = sum(VG_N) / sum_len
                        VR_N = [x[2] for x in pixel_sum]
                        VR_N = sum(VR_N) / sum_len

                        # VB_N = img[row][col - range_app][0]
                        # VG_N = img[row][col - range_app][1]
                        # VR_N = img[row][col - range_app][2]
                    except:
                        print(col, row)
                    if (VR_N > 180 and VB_N < 70 and VG_N < 70) or ((VR_N - VB_N) > 50 and (VR_N - VG_N) > 50):
                        continue
                    else:
                        img[row][col][0] = VB_N
                        img[row][col][1] = VG_N
                        img[row][col][2] = VR_N
    # cv2.imshow("delredcir", img)
    if loop_num == loop_max - 1:
        cv2.imwrite(OutputFile, img)


def access_pixels2(img, OutputFile, loop_num=1, loop_max = 2):
    """遍历图像每个像素的每个通道"""
    print(img.shape)              #打印图像的高，宽，通道数（返回一个3元素的tuple）
    height = img.shape[0]        #将tuple中的元素取出，赋值给height，width，channels
    width = img.shape[1]
    channels = img.shape[2]
    print("height:%s,width:%s,channels:%s" % (height,width,channels))
    print(img.size)              #打印图像数组内总的元素数目（总数=高X宽X通道数）

    range_app = 12

    for row in range(height):    #遍历每一行
        for col in range(width): #遍历每一列
            if col - range_app < 0 or row - range_app < 0 or col + range_app > 1919 or row + range_app > 1079:
                continue
            else:
                VB = int(img[row][col][0])
                VG = int(img[row][col][1])
                VR = int(img[row][col][2])
                if (VR > 180 and VB <70 and VG < 70) or ( (VR - VB) >50 and (VR - VG) > 50 ):
                    pixel_sum = []
                    for i_mean in range(1,range_app + 1):               # 求其上下左右各8个的像素的均值
                        for j_mean in range(1,range_app + 1):
                            pixel_sum.append(img[row - j_mean][col - i_mean])
                            pixel_sum.append(img[row - i_mean][col - j_mean])
                            pixel_sum.append(img[row + j_mean][col + i_mean])
                            pixel_sum.append(img[row + i_mean][col - j_mean])
                    try:
                        # sum_len = len(pixel_sum)
                        # VB_N = [x[0] for x in pixel_sum]
                        # VB_N = sum(VB_N) / sum_len
                        # VG_N = [x[1] for x in pixel_sum]
                        # VG_N = sum(VG_N) / sum_len
                        # VR_N = [x[2] for x in pixel_sum]
                        # VR_N = sum(VR_N) / sum_len

                        VB_N = img[row][col - range_app][0]
                        VG_N = img[row][col - range_app][1]
                        VR_N = img[row][col - range_app][2]
                    except:
                        print(col, row)
                    if (VR_N > 180 and VB_N < 70 and VG_N < 70) or ((VR_N - VB_N) > 50 and (VR_N - VG_N) > 50):
                        continue
                    else:
                        img[row][col][0] = VB_N
                        img[row][col][1] = VG_N
                        img[row][col][2] = VR_N
    if loop_num == loop_max - 1:
        cv2.imwrite(OutputFile, img)


def main():
    InputFile = "test1.jpg"
    MiddleFile = 'test_m.jpg'
    OutputFile = 'test8_dealed.jpg'

    pic = cv2.imread(InputFile)
    access_pixels1(pic, MiddleFile)
    # loop_max = 2
    # for i in range(loop_max):
    #     access_pixels(pic, i, loop_max)
    pic2 = cv2.imread(MiddleFile)
    access_pixels2(pic2, OutputFile)


if __name__ == '__main__':
    main()
