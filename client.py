# -*- coding:utf-8 -*-
import socket
import struct
import random
import threading
import time
from Util.socketutils import Client

# class Client:
#     __host = None
#     __port = None
#     dic ={'1':'lin','2':'li','3':'cao','4':'ji','5':'wu','6':'han','7':'fei','8':'mo','9':'lan','10':'cai'}
#
#     def __init__(self):
#         self.__host = '127.0.0.1'
#         self.__port = 5555
#
#     def send_message(self, n):
#         #data_res = ''
#         for i in range(n):
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             try:
#                 s.connect((self.__host, self.__port))  # 绑定地址和端口,必须跟客户端一样
#             except Exception as e:
#                 print('occur exception {}'.format(e))
#             #data_res = data_res+str(i)
#             rand=random.randint(1,10)
#             data_res ="insert into tbl values ({},\'{}\')".format(rand,self.dic[str(rand)])
#             self.fnSockSendMsg(s,data_res)
#             print(f"{i}发送数据成功{data_res}")
#             #s.sendall(data_res.encode())  # 发送信息
#         #self.fnSockSendMsg(s, 'close')
#             s.close()
#     def send_quit_message(self):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         try:
#             s.connect(('127.0.0.1', 5555))  # 绑定地址和端口,必须跟客户端一样
#         except Exception as e:
#             print('occur exception {}'.format(e))
#         self.fnSockSendMsg(s,'close')
#         s.close()
#
#     def fnSockSendMsg(self, conn, msg):
#         msg = msg.encode('utf-8')
#         dataHead = struct.pack('i', len(msg))  # 把消息长度打包成固定长度的bytes
#         conn.send(dataHead)  # 发送包头
#         conn.send(msg)  # 发送消息
#
#         # 获取消息，处理粘包
#
#     def fnSockGetMsg(self, conn):
#         dataHead = conn.recv(4)  # 先获取包头
#         dataLen = struct.unpack('i', dataHead)[0]  # 把包头解包成int类型
#         # 开始读取长度为 dataLen 的数据
#         recData = b''  # 获取到的消息
#         cacheLen = 1024  # 缓冲区大小
#         page = dataLen // cacheLen  # 分片
#         if page > 0:
#             for i in range(page):
#                 recData += conn.recv(cacheLen)
#             pageEnd = dataLen % cacheLen  # 最后一片
#             recData += conn.recv(pageEnd)
#         else:
#             recData += conn.recv(dataLen)
#         msg = recData.decode('utf-8')
#         return msg

# def fnSockGetMsg( conn):
#     dataHead = conn.recv(4)  # 先获取包头
#     dataLen = struct.unpack('i', dataHead)[0]  # 把包头解包成int类型
#         # 开始读取长度为 dataLen 的数据
#     recData = b''  # 获取到的消息
#     cacheLen = 1024  # 缓冲区大小
#     page = dataLen // cacheLen  # 分片
#     if page > 0:
#         for i in range(page):
#             recData += conn.recv(cacheLen)
#         pageEnd = dataLen % cacheLen  # 最后一片
#         recData += conn.recv(pageEnd)
#     else:
#         recData += conn.recv(dataLen)
#     msg = recData.decode('utf-8')
#     return msg
if __name__ == '__main__':
    client = Client(host='127.0.0.1',port=3333)
    client.send_message_num(10)
    #client.send_message(10)
    # m =random.randint(10,1000)
    # n =random.randint(10,1000)
    # print(m,n)
    # t1=threading.Thread(target=client.send_message,args=(m,))
    # t2 = threading.Thread(target=client.send_message, args=(n,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # client.send_quit_message()
    # print('wait exit')
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind(('127.0.0.1', 6666))
    # s.listen()
    # while True:
    #     try:
    #         connection, address = s.accept()
    #         data = fnSockGetMsg(connection)
    #         if data == 'close':
    #             break
    #     except Exception as e:
    #         print('occur exception as {}'.format(e))
    #         break
    # print('exit')