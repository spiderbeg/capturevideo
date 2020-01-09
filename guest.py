# encoding: utf8
import socket
import asyncio
import websockets
import json
import time
import numpy as np
import cv2
import sys
import threading
import queue
import settings

# 1 单连接客户端多线程版本
def receive():
    """接收视频图像信息"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((settings.HOST,settings.PORT))
        data = True
        while data:
            data = s.recv(216800)
            q.put(data) # 向队列中放置数据
            print('length: ',q.qsize())
        

def video():
    """显示每一帧图像"""
    while True:
        data = q.get(timeout=2) # 获取队列数据
        if data:
            image = np.asarray(bytearray(data), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            try:
                cv2.imshow('image',image)
            except cv2.error as e: # 接收图片数据出现损坏
                print('log:',e)
                continue
        if cv2.waitKey(35) & 0xFF == ord('q') or cv2.getWindowProperty('image', 0)<0: # 获取到键盘按下 'q' 键
            break

# 队列，遵循先进先出原则
q = queue.Queue(maxsize=20)
# 开启视频录制线程
t = threading.Thread(target=receive)
# 设置守护线程。当没有存活的非守护线程，程序退出。
# 服务端关闭连接时，退出
t.daemon = True
t.start()
# 显示传输的图片信息
video() 


# 2 单连接客户端异步版本
# async def receive():
#     """接收视频图像信息"""
#     # global r
#     HOST = '172.16.2.88' # 服务器地址
#     PORT = 65432 # 服务器端口
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST,PORT))
#         data = True
#         while True:
#             await asyncio.sleep(0.05)
#             data = await recvs(s)
#             q.put(data)
#             print('length: ',q.qsize())
        
# async def recvs(s):
#     return s.recv(216800) # 缓存区数据大小限制  

# async def video():
#     """显示每一帧图像"""
#     # global r
#     while True:
#         print('执行否？')
#         if q.empty():
#             await asyncio.sleep(0.05)
#             continue
#         data = q.get(timeout=2)
#         asyncio.sleep(0.05)
#         if data:
#             image = np.asarray(bytearray(data), dtype="uint8")
#             image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#             try:
#                 image = cv2.resize(image, (480,360), interpolation = cv2.INTER_AREA)
#             except cv2.error as e:
#                 print('log: ', e)
#                 continue
#             cv2.imshow('image',image)
#         if cv2.waitKey(1) & 0xFF == ord('q'): # 获取到键盘按下 'q' 键
#             break
# async def main():
#     # 并发运行可等待对象。如果可等待对象为协程，则自动作为一个任务加入日程
#     await asyncio.gather(
#         receive(),
#         video(),
#     )
# # 在内部队列使用锁，来临时阻塞竞争线程
# q = queue.Queue(maxsize=5)
# asyncio.run(main())









