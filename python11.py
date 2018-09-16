from multiprocessing import process
from os import getpid
from random import randint
from threading import Thread
from time import time, sleep


class Task(Thread):

    def __init__(self,name):
        super().__init__()
        self._name = name

    def run(name):
        print('当前进程号[%d]' % getpid())
        print('开始下载%s' % name)
        time = randint(5, 10)
        sleep(time)
        print('%s 下载完成，耗时%d秒' % (name, time))

def main():
    start = time()
    p1 = Task('xx')
    p1.start()
    p2 = Task('yy') # Thread(target=task,args=('xx',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(end - start)


if __name__ == '__main__':
    main()