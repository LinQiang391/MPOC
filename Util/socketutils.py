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
        try:
            connection.send(head)  # 发送包头
            connection.send(msg)
        except Exception as e:
            print(f'send message failed,exceptiom as {e}')# 发送消息

        # 获取消息，处理粘包

    def get_message(self, connection):
        try:
            head = connection.recv(4)
            length = struct.unpack('i', head)[0]
        except Exception as e:
            return None
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

    def create_socket(self, bind: bool = True, host: str = None, port: int = None):
        if host is None:
            host = self.__host
        if port is None:
            port = self.__port
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if bind:
            connection.bind((host, port))
        else:
            connection.connect((host, port))

        return connection

    def send_close_message(self, connection: socket = None):
        if connection is None:
            return
        else:
            self.send_message(connection, 'close')


class Server(Socket):

    def __init__(self, host: str = '127.0.0.1', port: int = 3333):
        super(Server, self).__init__(host, port)

    #单个socket完成消息客户端与服务端消息的交互，只允许与单个客户端通信，绑定相同个端口
    def server_start_with_single_socket(self):
        s = self.create_socket()
        s.listen()
        connection, address = s.accept()
        while True:
            try:
                message = self.get_message(connection=connection)
                if message is not None:
                    if message == 'close':
                        connection.close()
                        s.close()
                        return
                    else:
                        print(message)
            except Exception as e:
                print(f'occur exception {e}')
                connection.close()
                s.close()
                return
        connection.close()
        s.close()

    def server_start_with_differ_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 3333))
        s.listen()
        num = 0
        # connection, address =s.accept()
        l = []
        while True:
            try:
                connection, address = s.accept()
                data = self.get_message(connection)
                if data == 'close':
                    pass
                    # self.__redis.close()
                    #self.send_quit_message()
                else:
                    print(data)
            except Exception as e:
                print('occur exception as {}'.format(e))
                break

    def server_start(self, connection: socket = None, single: bool = True):
        if connection is None:
            connection = self.create_socket(bind=True)
        connection.listen()

        if single:
            new_connection, address = connection.accept()
        while True:
            try:
                if not single:
                    new_connection, address = connection.accept()
                message = self.get_message(connection=new_connection)
                if message is not None:
                    if message == 'close':
                        new_connection.close()
                        connection.close()
                        return
                    else:
                        print(message)
            except Exception as e:
                print(f'occur exception {e}')
                new_connection.close()
                connection.close()
                return


class Client(Socket):

    def __init__(self, host: str = '127.0.0.1', port: int = 3333):
        super(Client, self).__init__(host, port)

    def send_message_from_list(self, connection: socket = None, msgs: list = None, close: bool = True) -> bool:
        if connection is None:
            for msg in msgs:
                connection = self.create_socket(bind=False)
                try:
                    self.send_message(connection, msg)
                    print(msg)
                except Exception as e:
                    print(f'occur exception as {e}')
                    return False
                connection.close()
        else:
            for msg in msgs:
                try:
                    self.send_message(connection,msg)
                except Exception as e:
                    return False
            if close:
                connection.close
        return True