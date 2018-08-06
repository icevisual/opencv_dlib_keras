# _*_ coding:UTF-8 _*_  
import win32con
import win32api
import random
import ctypes
import ctypes.wintypes
import threading
import time
import os
import sys
from winapi import window_capture
from other.cv2_t2 import get_can_cant_use
from other.cv2_t3 import read_img_p_count
from icevisual.Utils import Utils

RUN = False  # 用来传递运行一次的参数
EXIT = False  # 用来传递退出的参数
user32 = ctypes.windll.user32  # 加载user32.dll
id1 = 105  # 注册热键的唯一id，用来区分热键
id2 = 106


class HotkeyThread(threading.Thread):  # 创建一个Thread.threading的扩展类

    def RunSomething(self, trytime):
        VK_E = 0x45
        VK_R = 0x52
        VK_ESCAPE = win32con.VK_ESCAPE
        VK_UP = win32con.VK_UP
        VK_RIGHT = win32con.VK_RIGHT
        DefaultSleep = 100
        vks = [VK_ESCAPE, 0xff + 200, VK_E, 0xff + DefaultSleep, VK_UP, 0xff + DefaultSleep, VK_E, 0xff + DefaultSleep, \
               VK_E, 0xff, VK_ESCAPE, 0xff + DefaultSleep, VK_RIGHT,
               0xff + DefaultSleep, VK_E, 0xff + 200, VK_E, 0xff + 200, VK_E, 0xff + 300, VK_E, 0xff + 300, VK_E,
               0xff + 300, VK_E, 0xff + 300, VK_E, 0xff + 300, VK_E, ]

        for j in range(0, trytime):
            for i in range(0, len(vks)):
                if vks[i] == 0xff:
                    r = random.randint(28.32)
                    print("Sleep %d" % r)
                    time.sleep(r / 1000.0)
                elif vks[i] < 0xff:
                    win32api.keybd_event(vks[i], 0, 0, 0)
                    win32api.keybd_event(vks[i], 0, win32con.KEYEVENTF_KEYUP, 0)
                else:
                    time.sleep((vks[i] - 0xff) / 1000.0)
            if j < trytime - 1:
                time.sleep(5)

    def RunMain(self):
        
        pass

    def run_id1(self):
        filename = "storage/ScreenShot/%d.jpg" % time.time();
        window_capture(filename)
        get_can_cant_use(filename, 'storage/ScreenShot/UseDisableEnable.jpg')
        os.unlink(filename)

        '''
w = 1600 h=900
Counr =  1842   enable
2018-08-05 23:27:00.050 Run ID1
RUNNING
w = 1600 h=900
Counr =  3284   disable
2018-08-05 23:27:16.142 Run ID1'''

        read_img_p_count('storage/ScreenShot/UseDisableEnable.jpg')
        print(Utils.format_time_with_millisecond(), "Run ID1")

    def run(self):
        global EXIT  # 定义全局变量，这个可以在不同线程间共用。
        global RUN  # 定义全局变量，这个可以在不同线程间共用。

        if not user32.RegisterHotKey(None, id1, 0, win32con.VK_F9):
            # 注册快捷键F9并判断是否成功，该热键用于执行一次需要执行的内容。
            print("Unable to register id", id1)  # 返回一个错误信息

        if not user32.RegisterHotKey(None, id2, 0, win32con.VK_F10):
            # 注册快捷键F10并判断是否成功，该热键用于结束程序，且最好这么结束，否则影响下一次注册热键。
            print("Unable to register id", id2)

        # 以下为检测热键是否被按下，并在最后释放快捷键
        try:
            msg = ctypes.wintypes.MSG()
            while True:
                if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                    if msg.message == win32con.WM_HOTKEY:
                        if msg.wParam == id1:
                            RUN = True
                            self.run_id1()
                        elif msg.wParam == id2:
                            EXIT = True
                            return
                    user32.TranslateMessage(ctypes.byref(msg))
                    user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            # 必须得释放热键，否则下次就会注册失败，所以当程序异常退出，没有释放热键，
            user32.UnregisterHotKey(None, id1)
            # 那么下次很可能就没办法注册成功了，这时可以换一个热键测试
            user32.UnregisterHotKey(None, id2)


if __name__ == "__main__":
    print(time.time())
    r = random.randint(28, 32)
    print(r)
    time.sleep(r / 1000.0)
    print(time.time())

    sys.exit();
    hotkey = HotkeyThread()
    hotkey.start()

    while True:
        if RUN:
            # 这里放你要用热键启动执行的代码
            print("RUNNING")
            RUN = False

        elif EXIT:
            # 这里是用于退出循环的
            break
