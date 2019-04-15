# coding:utf8
# Author :       huxiaoyi
# Date：         2019-04-15
# Time：         03:31
import threading
import time


def loop():
    print("thread %s is runing" % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
print('thread %s ended.' % threading.current_thread().name)
t = threading.Thread(target=loop,name="LoopThread")
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
