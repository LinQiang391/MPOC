# -*- coding:utf-8 -*-
import socket
import struct
import random
import threading

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
            print(f'send message failed,exceptiom as {e}')

    def get_message(self, connection):
        try:
            connection.settimeout(1)            #设置超时时间，避免只有连接没有发送消息，导致进程阻塞
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

class Server(Socket):

    def __init__(self, host: str = '127.0.0.1', port: int = 3333):
        super(Server, self).__init__(host, port)



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
                    #print(address)
                message = self.get_message(connection=new_connection)
                if message is not None:
                    if message == 'close':
                        new_connection.close()
                        connection.close()
                        return
                    else:
                        print(message)
                else:
                    print('fail')
            except Exception as e:
                print(f'occur exception {e}')
                new_connection.close()
                connection.close()
                return


class Client(Socket):

    __lock=threading.Lock()

    def __init__(self, host: str = '127.0.0.1', port: int = 3333):
        super(Client, self).__init__(host, port)

    def __send_message_from_list(self, connection: socket = None, msgs: list = None, close: bool = True) -> bool:
        if connection is None:
            for msg in msgs:
                connection = self.create_socket(bind=False)
                self.__lock.acquire()
                self.send_message(connection=connection,msg=msg)
                print(msg)
                self.__lock.release()
                #如果连接不关闭，需要后续处理
                if close:
                    connection.close()
        else:
            for msg in msgs:
                self.__lock.acquire()
                self.send_message(connection=connection, msg=msg)
                print(msg)
                self.__lock.release()
            if close:
                connection.close
        return True

    def __send_message_from_string(self, connection: socket = None, msg: str= None,close:bool =True):
        if connection is None:
            connection=self.create_socket(bind=False)
            self.__lock.acquire()
            self.send_message(connection=connection,msg=msg)
            print(msg)
            self.__lock.release()
            if close:
                connection.close()
        else:
            self.__lock.acquire()
            self.send_message(connection=connection,msg=msg)
            print(msg)
            self.__lock.release()
            if close:
                connection.close()

    def send_message_ex(self, connection: socket=None, msg = None, close: bool=True):

        if isinstance(msg, list):
            self.__send_message_from_list(connection=connection,msgs=msg,close=close)
        elif isinstance(msg,str):
            self.__send_message_from_string(connection=connection,msg=msg,close=close)
        else:
            print('type error')
