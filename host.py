# -*- coding: utf-8 -*-
import socket
import sys
import time

import cv2

import settings # 导入配置文件

# 1 单连接服务端端

# 建立 tcp 类型的 socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 1 将socket和地址绑定，且socket未被绑定
    s.bind((settings.HOST, settings.PORT))
    # 2 允许服务端接收连接，参数 backlog 表示允许的连接数量
    s.listen()
    # 3 接受一个连接，socket 必须绑定一个地址，并监听连接
    # conn,address 
    # conn 是返回的能够发送和接受连接数据的新 socket 对象
    # addr 客户端地址（主机地址，端口号）
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        # 4.1 opencv 展示视频并获取视频信息
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) # 一般对于电脑来说 0，就是代表自带的摄像头设备
        cap.set(3,360)
        cap.set(4,240)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 80] # 压缩为 jpg，压缩等级好到坏（100-0）
        while cap.isOpened():
            t1 = time.time()
            # 4.2 逐帧获取图片
            ret, frame = cap.read() # ret: 布尔值，表示是否读取正确；frame：图片信息，类型：numpy 数组 
            # 4.3 获取图片数据并压缩为 jpg 格式
            # 4.3.1 将 frame 压缩为 jpg 格式
            success, encoded_image = cv2.imencode('.jpg', frame, encode_param)
            # 4.3.2 转换为字节
            content2 = encoded_image.tobytes()
            # 4.3.3 展示结果
            cv2.imshow('frame',frame)
            
            if cv2.waitKey(35) & 0xFF == ord('q') or cv2.getWindowProperty('frame', 0)<0:
                break
            print('time: ', time.time()-t1)
        
            # 5 socket 发送数据到客户端
            # 获取到的图像数据
            # 持续发送数据直到数据发送完毕
            # 发送成功返回 None 
            conn.sendall(content2)
        # 最后，释放占用的摄像机资源及关闭窗口
        cap.release()
        cv2.destroyAllWindows()