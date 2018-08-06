import cv2
import numpy as np
import sys

basepath = "../storage/ScreenShot/"


def get_subimg_in_middle(filename, distfile, target_width, ys, ye):
    img = cv2.imread(filename)
    w = len(img[0])
    h = len(img)
    print("w = %d h=%d" % (w, h))
    sx = int((w - target_width) / 2)
    ex = int((w + target_width) / 2)
    # 使用部分
    frame = img[ys:ye, sx:ex]
    cv2.imwrite(distfile, frame)

    # cv2.imshow('frame', frame)
    # cv2.moveWindow("frame", 0, 0)
    # cv2.imshow('dst', img)
    # cv2.moveWindow("dst", 0, 100)


def get_can_cant_use(filename, distfilename):
    get_subimg_in_middle(filename, distfilename, 360, 310, 350)


if __name__ == '__main__':
    get_subimg_in_middle(basepath + 'CantUse.jpg', basepath + 'UseDisable.jpg', 360, 310, 350)
    get_subimg_in_middle(basepath + 'CanUse.jpg', basepath + 'UseEnable.jpg', 360, 310, 350)
    get_subimg_in_middle(basepath + 'ConfirmNO.jpg', basepath + 'NoSelected.jpg', 760, 760, 810)
    get_subimg_in_middle(basepath + 'ConfirmYes.jpg', basepath + 'YesSelected.jpg', 760, 760, 810)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

#
# filename = basepath + 'ConfirmNO.jpg'
# img = cv2.imread(filename)
# # cv2.imshow('sss', img)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray, 2, 3, 0.04)
#
# # result is dilated for marking the corners, not important
# dst = cv2.dilate(dst, None)
#
# # Threshold for an optimal value, it may vary depending on the image.
# img[dst > 0.01 * dst.max()] = [0, 0, 255]
#
# cv2.imshow('dst', img)
# cv2.moveWindow("dst", 100, 500)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
