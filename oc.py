# 调用摄像头获取图像信息在一个窗口处展示，
import cv2
import time

 # 一般对于电脑来说 0，就是代表自带的摄像头设备,返回 VideoCapture 对象
cap = cv2.VideoCapture(0)
cap.set(3,280) # 设置 VideoCapture 对象属性宽
cap.set(4,200) # 设置高
while cap.isOpened():
    # cap.isOpened() 判断是否正确初始化
    # 逐帧获取图片
    ret, frame = cap.read() # ret: 布尔值，表示是否读取正确；frame：图片信息(数组对象 ndarray, 数据类型 np.int8), 
    # 在名为 frame 的窗口展示图片
    cv2.imshow('frame',frame)
    # 1.0 获取到键盘按下 'q' 键, 退出. cv2.getWindowProperty('frame', 0) 窗口关闭，退出
    # 1.1 cv2.waitKey(25) 可用于控制视频速度，等待25毫秒
    # 1.2 64 位电脑： cv2.waitKey(25) & 0xFF   32位电脑：cv2.waitKey(25)
    t1 = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q') or cv2.getWindowProperty('frame', 0)<0:
        break
    print('time: ',time.time()-t1)
# 最后，释放占用的摄像机资源
cap.release()
# 关闭窗口
cv2.destroyAllWindows()
