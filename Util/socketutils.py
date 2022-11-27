# -*- coding:utf-8 -*-
import socket
import struct
import random


class Socket:

    __host = None
    __port = None

    def __init__(self, host: str = '127.0.0.1', port: int = 3333):
        self.__host = host
        self.__port = port

    def send_message(self, connection, msg):
        msg = msg.encode('utf-8')
        head = struct.pack('i', len(msg))  # 把消息长度打包成固定长度的bytes
        connection.send(head)  # 发送包头
        connection.send(msg)  # 发送消息

        # 获取消息，处理粘包

    def get_message(self, connection):
        head = connection.recv(4)
        length = struct.unpack('i', head)[0]  # 把包头解包成int类型
        # 开始读取长度为 length 的数据
        recData = b''  # 获取到的消息
        cacheLen = 1024  # 缓冲区大小
        page = length // cacheLen  # 分片
        if page > 0:
            for i in range(page):
                recData += connection.recv(cacheLen)
            end = length % cacheLen  # 最后一片
            recData += connection.recv(end)
        else:
            recData += connection.recv(length)
        msg = recData.decode('utf-8')
        return msg

    def getHost(self):
        return self.__host

    def getPort(self):
        return self.__port

    def create_socket(self, bind: bool = True):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if bind:
            connection.bind((self.getHost(), self.getPort()))
        return connection


class Server(Socket):

    def __init__(self, host: str = '127.0.0.1', port: int = 3333):
        super(Server, self).__init__(host, port)

    def server_start(self):
        s = self.create_socket()
        s.listen()
        while True:
            try:
                connection, address = s.accept()
                message = self.get_message(connection=connection)
                if message == 'close':
                    connection.close()
                    s.close()
                    break
                else:
                    connection.close()
                    print(message)
            except Exception as e:
                print(f'occur exception {e}')
                s.close()
                break


class Client(Socket):

    def __init__(self, host: str = '127.0.0.1', port: int = 3333):
        super(Client, self).__init__(host, port)

    def send_message_num(self, n):
        for i in range(n):
            s = self.create_socket(bind=False)
            try:
                s.connect((self.getHost(), self.getPort()))
            except Exception as e:
                print('occur exception {}'.format(e))
            rand = random.randint(1, 10)
            data_res = "insert into tbl values {}".format(rand)
            self.send_message(s, data_res)
            print(f"{i}发送数据成功{data_res}")
            s.close()
