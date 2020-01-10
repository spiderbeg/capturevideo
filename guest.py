# encoding: utf8
import socket
import time
import threading
import queue

import cv2
import numpy as np

import settings

# 1 单连接客户端多线程版本
def receive():
    """接收视频图像信息"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 连接服务端
        s.connect((settings.HOST,settings.PORT))
        data = True
        while data:
            # 接收服务端发送的图片信息
            data = s.recv(216800)
            q.put(data) # 向队列中放置图片数据
            print('length: ',q.qsize())
        

def video():
    """显示每一帧图像"""
    while True:
        data = q.get(timeout=10) # 获取队列图片数据, 10秒后还没有数据则报错 
        # 将字节数据转换为数组，用于 opencv 读取信息。
        image = np.asarray(bytearray(data), dtype="uint8")
        # 读取图片信息
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        try:
            # 在名为 'image' 的窗口中显示图片信息
            cv2.imshow('image',image)
        except cv2.error as e: # 接收图片数据出现损坏
            print('log:',e)
            continue
        if cv2.waitKey(35) & 0xFF == ord('q') or cv2.getWindowProperty('image', 0)<0: # 获取到键盘按下 'q' 键，或关闭窗口
            # cv2.waitKey(35) 可用于控制速度，35表示等待 35 毫秒。
            break

# 队列，遵循先进先出原则
q = queue.Queue(maxsize=20)
# 开启视频录制线程
t = threading.Thread(target=receive)
# 设置守护线程。
# 服务端关闭连接时，退出
t.daemon = True
t.start()
# 显示传输的图片信息
video() 






