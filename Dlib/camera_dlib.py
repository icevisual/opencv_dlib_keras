# -*- coding:utf-8 -*-

import dlib
import cv2
import os
from icevisual.Utils import Marker

maker = Marker()

if __name__ == '__main__':
    current_path = os.getcwd()  # 获取当前路径
    # 模型路径
    predictor_path = current_path + "\\model\\shape_predictor_68_face_landmarks.dat"
    face_rec_model_path = current_path + "\\model\\dlib_face_recognition_resnet_model_v1.dat"
    # 测试图片路径
    faces_folder_path = current_path + "\\faces\\"

    # 读入模型
    detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor(predictor_path)
    face_rec_model = dlib.face_recognition_model_v1(face_rec_model_path)

    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        # opencv 读取图片，并显示
        img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        # opencv的bgr格式图片转换成rgb格式
        b, g, r = cv2.split(img)
        img2 = cv2.merge([r, g, b])

        dets = detector(img, 1)  # 人脸标定
        print("Number of faces detected: {}".format(len(dets)))

        color = (255, 255, 255)  # 白

        for index, face in enumerate(dets):
            print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(),
                                                                         face.bottom()))
            cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), color, thickness=2)
            maker.mark("before_predictor")
            shape = shape_predictor(img2, face)  # 提取68个特征点
            maker.mark("after_predictor")
            maker.distance("before_predictor", "after_predictor")

            for i, pt in enumerate(shape.parts()):
                # print('Part {}: {}'.format(i, pt))
                pt_pos = (pt.x, pt.y)
                cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
                # print(type(pt))
            # print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))
            # cv2.namedWindow(img_path + str(index), cv2.WINDOW_AUTOSIZE)
            cv2.imshow('Video', frame)
            maker.mark("before_compute_face_descriptorr")
            face_descriptor = face_rec_model.compute_face_descriptor(img2, shape)  # 计算人脸的128维的向量

            maker.mark("after_compute_face_descriptor")
            maker.distance("before_compute_face_descriptorr", "after_compute_face_descriptor")


            print(face_descriptor)



        cv2.imshow('Video', frame)
        #10msecキー入力待ち
        k = cv2.waitKey(100)
        #Escキーを押されたら終了
        if k == 27:
            break

    #キャプチャを終了
    cap.release()
    cv2.destroyAllWindows()
