import time
from Util.socketutils import Client
import threading

if __name__ == '__main__':
    client = Client(host='127.0.0.1', port=3333)
    # connection=client.create_socket(bind=False)
    l1=[]
    l2=[]
    for i in range (100):
        l1.append(str(i))
        l2.append(str(i*2))
    #client.send_message_from_list(connection=None,msgs=l1,close=True)
    #client.send_message_from_list(connection=None, msgs=l1, close=True)
    t1 = threading.Thread(target=client.send_message_from_list, args=(None, l1, True))
    t2 = threading.Thread(target=client.send_message_from_list, args=(None, l2, True))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('finished')
    # s=client.create_socket(bind=False)
    # for i in range(100):
    #     client.send_message_from_list(connection=s,msgs=[str(i)],close=False)
    #     client.send_message_from_list(connection=s,msgs=[str(i*2)],close=False)