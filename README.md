# MPOC
# 草稿：

### 1.绘制聊天窗口

1.使用PYQT绘制聊天窗口，后期UI优化可以借助其他技术。

## 2.实现消息收发

2.基于socket通信（可以设计定时消息？）

1.仍然存在问题：

​	基于单socket的通信

​	基于多socket的通信

​	基于单线程

​	基于多线程



实现类：

基类：定义服务端，客户端的实现接口。

基本属性：host,port

端口绑定，

消息收发发，(TCP连接需要处理数据沾包问题，UDP连接还需要处理，报文层面的暂不考虑)



1.子类：服务端，客户端



客户端向服务端发消息



socket.revc()函数默认为阻塞，可以socket.settimeout()设置该socket的超时时间，解决多线程问题是需要需要给socket资源加锁，否则对单个socket发送消息可能还是会出现粘包的问题。

测试场景：

1.单线程，单socket（通过）

2.多线程，单socket(通过)

3.单线程，多socket(通过)

4.多线程，多socket(通过)











## 3.聊天记录保存

3.使用DB文件存储聊天记录？
