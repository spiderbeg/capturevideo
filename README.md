# Python 视频传输
* 此教程介绍 Python 利用 OpenCV 调用摄像头获取数据并利用 socket 传输到局域网内另一台主机。
## 项目思路
1. OpenCV 调用摄像头获取视频信息。
2. socket 编程建立服务端客户端单连接模式；服务端使用 TCP 传输视频的每一帧图片信息到客户端，并在客户端播放视频。
## 快速上手
### 项目下载
确认放置项目的目录，运行以下命令：

    git clone https://github.com/spiderbeg/capturevideo
### 本机运行服务端和客户端
在自己电脑上运行，分别执行 host.py 和 guest.py 两个文件即可
### 局域网内两台电脑
* 发送视频信息的电脑运行运行 host.py(服务端), 显示视频信息的电脑运行 guest.py(客户端), 接收服务端发送的信息。
* 需要注意的是，两台电脑需要在同一局域网内，同时两台电脑都需要将 settings.py 中的 HOST 修改为服务端 IP 地址。控制台中输入以下命令可查看：

        # windows 
        ipconfig
        # linux
        ifconfig
## 运行环境
* Windows
* python 3.7
## 运行依赖包
* opencv
## 文件说明
* host.py: 服务端程序，负责监听客户端连接；调用摄像头并将视频信息以图片形式向客户端发送。以及 socket 相关的详细讲解。
* guest.py: 客户端程序，接收来自服务端的视频信息，并播放。
* settings.py: 程序的配置文件，服务端客户端都需要。若要在局域网内两台机子上测试，记得修改 host 为服务端 ip。
* oc.py: OpenCV 调用摄像头的简单实例。
## 部分建议
* opencv 安装，运行以下命令，

        pip install opencv-python
* socket 简单知识，详见 host.py。
* OpenCV 调用摄像头，详细见 oc.py。
* opencv-python 文档教程<https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html>。

 