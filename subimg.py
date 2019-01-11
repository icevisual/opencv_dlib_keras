import cv2
import sys
import os
import re




# #FF015198
# 

def color_similarity_clear(image, transparency_color_list, similarity = 0.6):
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            a1 = image[i][j][0] / transparency_color_list[0]
            a2 = image[i][j][1] / transparency_color_list[1]
            a3 = image[i][j][2] / transparency_color_list[2]
            a4 = image[i][j][3] / transparency_color_list[3]
            if a1 > similarity \
                    and a2 > similarity \
                    and a3 > similarity \
                    and a4 > similarity :
                image[i][j] = [0, 0, 0, 0]
    return image

def coloe_set(image, transparency_color_list):
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if image[i][j][0] > 0 \
                    or image[i][j][0] > 0 \
                    or image[i][j][0] > 0 \
                    or image[i][j][0] > 0 :
                image[i][j] = transparency_color_list
    return image

def color_set_alpha0():
    w = 4961 
    h = 3508
    image = cv2.imread("Template", -1)
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            image[i][j] = [0, 0, 0, 0]
    cv2.imwrite("aaa.png", image)


if __name__ == '__main__':
    # filename x y with height distname
    if len(sys.argv) >= 7:
        filename, x, y, w, h, distname = sys.argv[1:7]
        x = int(x) 
        y = int(y) 
        h = int(h) 
        w = int(w) 
        transparency = False
        if len(sys.argv) >= 8:
            transparency = True
            transparency_color = sys.argv[7]
            if re.match(r"[a-fA-F0-9]{8}", transparency_color):
                transparency_color_list = list(bytes.fromhex(transparency_color))
                transparency_color_list.reverse()
            else:
                transparency_color_list = [255, 255, 255, 255]
        if os.path.isfile(filename):
            frame = cv2.imread(filename, -1)
            # pnt(len(frame))
            print(len(frame[0][0]))
            image = frame[y:y + h, x: x + w]
            similarity = 0.6
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            if transparency:
                color_similarity_clear(image, transparency_color_list, similarity)
                # coloe_set(image, list(bytes.fromhex("FFffffff")))
            cv2.imwrite(distname, image)
            # cv2.imshow("Result",frame)
            # FF 0C 64 B6
            # A  R   G  B
            # 255 12 100 182
            # [182 100  12 255]
            # B    G     R   A
            cv2.waitKey(0)
        else:
            print("Source File Not Exists")
    else:
        print("ARGV Number Error")
