# -*- coding:utf-8 -*-

import socket
import struct
import redis
import pymysql
from Util.socketutils import Server

if __name__ == '__main__':
    server = Server()
    #server.server_start_with_differ_socket()
    server.server_start(single=False)
