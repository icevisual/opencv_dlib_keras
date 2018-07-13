from imutils import face_utils
import argparse
import imutils
import dlib
import cv2
import index


def takephoto():
    cap = cv2.VideoCapture(0)
    while (1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键完成照相
            # cv2.imwrite("./test0.jpg", frame) 保存照片，但在这里我们并不需要
            return frame  # 返回图片
    cap.release()
    cv2.destroyAllWindows()


def main():
    # construct the argument parser and parse the arguments 使用argparse设置输入所需的实参
    ap = argparse.ArgumentParser()
    # ap.add_argument("-p", "--shape-predictor", required=True, #训练好的关于检测的文件
    #                 help="path to facial landmark predictor")
    ap.add_argument("-i", "--image", required=False, default='0',  # 图片
                    help="path to input image")
    args = vars(ap.parse_args())

    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    # 初始化dlib人脸检测（基于HOG），然后创建面部标志预测器
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(index.storage_path("model\\shape_predictor_68_face_landmarks.dat"))

    # load the input image, resize it, and convert it to grayscale
    if args['image'] != '0':
        image = cv2.imread(args['image'])  # 输入图片实参则读入图片
    else:
        image = takephoto()  # 若未输入则进行照相操作

    image = imutils.resize(image, width=500)  # 调整图片宽度为500
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 图片调整为灰色

    # detect faces in the grayscale image 检测灰度图像中的面部
    rects = detector(gray, 1)

    # loop over the face detections 循环进行人脸的检测
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        # 确定面部区域的面部标志，然后将面部标志（x，y）坐标转换成NumPy阵列
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # convert dlib's rectangle to a OpenCV-style bounding box
        # [i.e., (x, y, w, h)], then draw the face bounding box
        # 将dlib矩形转换为OpenCV样式的边界框[即（x，y，w，h）]，然后绘制边界框
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # show the face number 人脸序号的标记（可识别多张）
        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        # 循环找到面部地关键点的（x，y）坐标并在图像上绘制它们
        for (x, y) in shape:
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

    # show the output image with the face detections + facial landmarks
    # 用脸部检测+面部标志显示输出图像
    cv2.imshow("Output", image)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
