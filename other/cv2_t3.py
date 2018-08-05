import cv2
import numpy as np


def count_point(img):
    count_1 = 0
    for y in range(0, len(img)):
        for x in range(0, len(img[0])):
            #  9 26 69
            if abs(img[y][x][0] - 9) < 10 and \
                    abs(img[y][x][1] - 26) < 10 and \
                    abs(img[y][x][2] - 70) < 10:
                img[y][x] = [0, 0, 0]
            else:
                count_1 += 1
                # print(img[y][x], end=" ")
        # print()
    print("Counr = ", count_1)


def read_img_p_count(filename):
    basepath = "../storage/ScreenShot/"
    img = cv2.imread(filename)
    count_point(img)
    return img


if __name__ == '__main__':
    basepath = "../storage/ScreenShot/"
    img = read_img_p_count('UseDisable.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('sss')
    cv2.moveWindow("sss", 0, 0)
    cv2.namedWindow('ddd')
    cv2.moveWindow("ddd", 100, 100)

    cv2.imshow("sss", img)

    count_point(img)

    cv2.imshow("ddd", img)
    cv2.waitKey()
