# -*- coding:utf-8 -*-
import time
from Util.socketutils import Client
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

if __name__ == '__main__':
    client = Client(host='127.0.0.1', port=3333)
    l1 = []
    for i in range(100):
        l1.append(str(i))

    task_list = []
    threadpool = ThreadPoolExecutor(5)
    single = False
    if single:
        s = client.create_socket(bind=False)
    for msg in l1:
        # 单socket通信
        if single:
            task_list.append(threadpool.submit(client.send_message_ex, s, msg, False))
        else:
            task_list.append(threadpool.submit(client.send_message_ex, None, msg, True))

    # 等待线程池中所有任务完成
    for result in as_completed(task_list):
        res = result.result()

    print(len(task_list))
