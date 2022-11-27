# -*- coding:utf-8 -*-

import socket
import struct
import redis
import pymysql
from Util.socketutils import Server
CFG = {
    'db_host': '127.0.0.1',
    'db_user': 'root',
    'db_password': 'Admin@123',
    'db_port': 3306
}

# class DBUtil:
#     __host = CFG['db_host']
#     __user = CFG['db_user']
#     __password = CFG['db_password']
#     __port = CFG['db_port']
#     __connection = None
#
#     def __get_db_cursor(self):
#         try:
#             self.__connection = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__password,
#                                                 port=self.__port)
#             cursor = self.__connection.cursor()
#             return cursor
#         except Exception as e:
#             print('connected failed ,Exception: {}'.format(e))
#
#     def execute_sql(self, all_sql: list = None):
#         result = []
#         if all_sql is None:
#             return None
#         else:
#             cur = self.__get_db_cursor()
#             for sql in all_sql:
#                 assert isinstance(sql, str), print('type of sql should be str')
#                 try:
#                     cur.execute('use test;')
#                     cur.execute(sql)
#                     res = cur.fetchall()
#                     result.append(res)
#                     self.__connection.commit()
#                 except Exception as e:
#                     self.__connection.rollback()
#                     print('executed \'{}\' failed, Exception:{}'.format(sql, e))
#                     result.append(())
#             self.__connection.close()
#             return result
#
# class Redis:
#     __host='127.0.0.1'
#     __port=6379
#     r=redis.Redis(host=__host,port=__port)
#     def setkey(self,key,value):
#         self.r.set(key,value)
#     def close(self):
#         self.r.close()
#

#
# class Server:
#     __host = None
#     __port = None
#     __dbutil=DBUtil()
#     # __redis=Redis()
#     def __init__(self):
#         self.__host = '127.0.0.1'
#         self.__port =5555
#
#     def receive_message(self):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.bind(('127.0.0.1', 5555))
#         s.listen()
#         num=0
#         #connection, address =s.accept()
#         l=[]
#         while True:
#             try:
#                 connection, address = s.accept()
#                 data = self.fnSockGetMsg(connection)
#                 if data == 'close':
#                     #pass
#                     #self.__redis.close()
#                     self.send_quit_message()
#                 else:
#                     print(data, num)
#                     l.append(data)
#                     self.__dbutil.execute_sql(l)
#                     l.pop(0)
#                     #self.__dbutil.execute_sql(data)
#                     #self.__redis.setkey(key=num,value=data)
#                     try:
#                         r=redis.Redis(host='127.0.0.1',port=6379)
#                         r.set(str(num),data)
#                         print('insert in redis success')
#                         r.close()
#                         num=num+1
#                     except Exception as e:
#                         print(f'connect redis failed err:{e}')
#                         r.close()
#                         break
#             except Exception as e:
#                 print('occur exception as {}'.format(e))
#                 break
#
#     def send_quit_message(self):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         try:
#             s.connect(('127.0.0.1', 6666)) # 绑定地址和端口,必须跟客户端一样
#         except Exception as e:
#             print('occur exception {}'.format(e))
#         self.fnSockSendMsg(s, 'close')
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


if __name__ == '__main__':
    server = Server()
    server.server_start()
