# -*- coding:utf-8 -*-
import cv2

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cascade_path = "../storage/haarcascades/haarcascade_frontalface_default.xml"

    while True:
        _, frame = cap.read()
        # グレースケール変換
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # カスケード分類器の特徴量を取得する
        cascade = cv2.CascadeClassifier(cascade_path)
        # 物体認識（顔認識）の実行
        minWith = 30
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(minWith, minWith))
        if len(facerect) > 0:
            print('face detected')
            color = (255, 255, 255)  # 白
            for rect in facerect:
                # 検出した顔を囲む矩形の作成
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                x, y = rect[0:2]
                width, height = rect[2:4]
                image = frame[y - 10: y + height, x: x + width]

        cv2.imshow("Video",frame)
        #10msecキー入力待ち
        k = cv2.waitKey(100)
        #Escキーを押されたら終了
        if k == 27:
            break

    #キャプチャを終了
    cap.release()
    cv2.destroyAllWindows()
