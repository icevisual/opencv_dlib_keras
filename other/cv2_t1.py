import os
import sys
import platform
import numpy as np
import cv2 as cv
import matplotlib.pyplot as mp
import mpl_toolkits.axes_grid1 as mg


# image = cv.imread('/Users/youkechaung/Desktop/算法/数据分析/AI/day02/day02/data/penguin.jpg')

def read_image(filename):
    image = cv.imread(filename)
    return image


def show_image(title, image):
    cv.imshow(title, image)


def calc_features(image):
    star = cv.xfeatures2d.StarDetector_create()
    keypoints = star.detect(image)
    sift = cv.xfeatures2d.SIFT_create()
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    keypoints, desc = sift.compute(gray, keypoints)
    # 返回的值为新的关键点和特征值矩阵
    print(desc.shape)
    return desc


def show_chart():
    mp.show()


def draw_desc(desc):
    ma = mp.matshow(desc, cmap='jet')
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('DESC', fontsize=20)
    mp.xlabel('Feature', fontsize=14)
    mp.ylabel('Sample', fontsize=14)
    ax = mp.gca()
    ax.xaxis.set_major_locator(mp.MultipleLocator(8))
    ax.xaxis.set_major_locator(mp.MultipleLocator())
    ax.yaxis.set_major_locator(mp.MultipleLocator(8))
    ax.yaxis.set_major_locator(mp.MultipleLocator())
    mp.tick_params(which='both', top=True, right=True, labelsize=10)
    dv = mg.make_axes_locatable(ax)
    ca = dv.append_axes('right', '3%', pad='3%')
    cb = mp.colorbar(ma, cax=ca)
    cb.set_label('DESC', fontsize=14)


def main(argc, argv, envp):
    original = read_image('/Users/youkechaung/Desktop/算法/数据分析/AI/day02/day02/data/penguin.jpg')
    show_image('Original', original)
    desc = calc_features(original)
    draw_desc(desc)
    show_chart()
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))
