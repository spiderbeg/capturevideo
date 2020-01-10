# Python 视频传输
* 此教程介绍 Python 利用 OpenCV 调用摄像头获取数据并利用 socket 传输到局域网内另一台主机。
* 更多实用而有趣的分析案例请关注：**Crossin的编程教室**
## 项目思路
1. OpenCV 调用摄像头获取视频信息, 将获取的每一帧图片信息压缩为 jpg 格式，以字节发送给客户端。
2. socket 编程建立服务端客户端单连接模式；服务端使用 TCP 传输视频的每一帧图片信息到客户端，并在客户端将接收到的信息转成 opencv 能够读取的格式并显示出来。
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
* numpy
## 文件说明
* host.py: 服务端程序，负责监听客户端连接；调用摄像头并将视频信息以图片形式向客户端发送。以及 socket 相关的详细讲解。
* guest.py: 客户端程序，接收来自服务端的视频信息，并播放。
* settings.py: 程序的配置文件，服务端客户端都需要。若要在局域网内两台机子上测试，记得修改 host 为服务端 ip。
* oc.py: OpenCV 调用摄像头的简单实例。
## 部分代码展示
以下为部分代码展示。完整示例见 host.py, guest.py, oc.py。
* 服务端监听端口，并发送数据

        # 服务端建立 tcp 类型的 socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # 1 将socket和地址绑定，且socket未被绑定
            # settings.HOST, settings.PORT 分别为服务端 IP 和 端口
            s.bind((settings.HOST, settings.PORT))
            # 2 允许服务端接收连接，参数 backlog 表示允许的连接数量
            s.listen()
            # 3 接受一个连接，socket 必须绑定一个地址，并监听连接
            # 返回值：conn,address 
            # conn 是返回的能够发送和接受连接数据的新 socket 对象
            # addr 客户端地址（主机地址，端口号）
            conn, addr = s.accept()

            # 省略中间部分...
            # 发送图片数据
            conn.sendall(content2)
* 客户端连接服务端, 并接收数据

        # 客户端连接服务端
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # 连接服务端。settings.HOST, settings.PORT 分别为服务端 IP 和 端口
            s.connect((settings.HOST,settings.PORT))

            # 省略中间部分。。。
            # 接收服务端发送的图片信息
            data = s.recv(216800)
* 服务端图片压缩

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 80] # 压缩为 jpg，压缩等级好到坏（100-0）
        # 4.2 逐帧获取图片
        ret, frame = cap.read() # ret: 布尔值，表示是否读取正确；frame：图片信息，类型：numpy 数组 
        # 4.3 获取图片数据并压缩为 jpg 格式
        # 4.3.1 将 frame 压缩为 jpg 格式
        success, encoded_image = cv2.imencode('.jpg', frame, encode_param)
        # 4.3.2 转换为字节
        content2 = encoded_image.tobytes()
* 客户端获取图片信息，并转换为 opencv 可读格式

        # 将字节数据转换为数组，用于 opencv 读取信息。
        image = np.asarray(bytearray(data), dtype="uint8")
        # 读取图片信息
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
* 客户端程序中使用一个线程接收服务端发送的数据，一个线程将数据用 opencv 展示，以下为多线程使用的简单示例

        import threading
        import time
        def go():
            time.sleep(1)
            print('这是新建线程')
        # 创建线程
        t = threading.Thread(target=go)
        # 开始运行线程
        t.start()
        print('这是主线程 ')
## 部分建议
* opencv 安装，运行以下命令，

        pip install opencv-python
* socket 部分操作，详见 host.py。
* OpenCV 调用摄像头操作，详细见 oc.py。
* opencv-python 文档教程<https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html>。
## Crossin的编程教室
* 更多实用而有趣的分析案例请关注：**Crossin的编程教室** <br>
<img src="Crossin的编程教室.jpg" alt="Crossin的编程教室.jpg" height="200" width="200">   
 