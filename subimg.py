import cv2
import sys
import os
import re

if __name__ == '__main__':
    # filename x y with height distname
    if len(sys.argv) >= 7:
        filename, x, y, w, h, distname = sys.argv[1:7]
        x = int(x) * 2
        y = int(y) * 2
        h = int(h) * 2
        w = int(w) * 2
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
            # print(len(frame))
            # print(len(frame[0]))
            image = frame[y:y + h, x: x + w]
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            if transparency:
                for i in range(0, len(image)):
                    for j in range(0, len(image[i])):
                        if image[i][j][0] == transparency_color_list[0] \
                                and image[i][j][1] == transparency_color_list[1] \
                                and image[i][j][2] == transparency_color_list[2] \
                                and image[i][j][3] == transparency_color_list[3]:
                            image[i][j] = [0, 0, 0, 0]
                        # print("[%d, %d]" % (i, j) , image[i][j])
                    # break
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
