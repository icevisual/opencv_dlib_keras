# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file '1.ui'
#
# Created: Tue Nov 14 09:45:29 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
# -*- coding: cp936 -*-
import cv2
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import sys
from icevisual.Utils import Utils

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    label = None
    label_2 = None
    button_screenshot = None

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1360, 640)

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(700, 10, 640, 480))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.button_screenshot = QtGui.QPushButton(Dialog)
        self.button_screenshot.setGeometry(QtCore.QRect(130, 500, 75, 23))
        self.button_screenshot.setObjectName(_fromUtf8("截图1"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "视频", None))
        self.label_2.setText(_translate("Dialog", "截图", None))
        self.button_screenshot.setText(_translate("Dialog", "截图1", None))
        self.button_screenshot.clicked.connect(self.camer_screenshot)

    def camer_screenshot(self):
        global cap
        ret, frame = cap.read()
        newfile = 'shotcut/' + Utils.timestamp_string() + '.jpg'
        cv2.imwrite(newfile, frame)
        # cv2.imshow('frame', frame)
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(newfile)))


    def open_camer(self):
        global cap, timer
        cap = cv2.VideoCapture(0)
        timer.start(100)
        # fourcc = cv2.cv.CV_FOURCC(*'XVID')
        # opencv3的话用:fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))#保存视频
        '''
        while True:
            ret,frame = cap.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            out.write(frame)#写入视频
            cv2.imshow('frame',frame)#一个窗口用以显示原视频
            cv2.imshow('gray',gray)#另一窗口显示处理视频
            if cv2.waitKey(1) &0xFF == ord('q'):
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        '''


class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        global timer
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)
        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.updtTime)
        self.ui.open_camer()

    def updtTime(self):
        global cap
        # cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        cascade_path = "haarcascades/haarcascade_frontalface_default.xml"
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        # facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))
        if len(facerect) > 0:
            print('face detected')
            color = (255, 255, 255)  # 白
            for rect in facerect:
                # 検出した顔を囲む矩形の作成
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                x, y = rect[0:2]
                width, height = rect[2:4]
                image = frame[y - 10: y + height, x: x + width]

                newfile = 'shotcut/' + Utils.timestamp_string() + '.jpg'
                cv2.imwrite(newfile, image)


        cv2.imwrite('1.jpg', frame)
        # out.write(frame)
        self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8('1.jpg')))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Dialog()
    myapp.show()
    app.exec_()
    pass
