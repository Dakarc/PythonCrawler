import time
import threading
import random

gMoney = 1000
gLock = threading.Lock()
gTotalTime = 10
gTime = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gTime >= 10:
                gLock.release()
                break
            gMoney += money
            print("%s生产了%d元,剩余%d元钱" % (threading.current_thread(),money,gMoney))
            gTime += 1
            gLock.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print("%s消费者消费了%d元,剩余%d元" % (threading.current_thread(),money,gMoney))
            else:
                if gTime >= gTotalTime:
                    gLock.release()
                    break
                print("%s消费者准备花费%d元钱,剩余%d元钱,不足" % (threading.current_thread(),money,gMoney))
                print("--gTime---是%d" % gTime)
                gLock.release()
                time.sleep(0.5)

def main():
    for x in range(3):
        t = Consumer(name='消费线程%d' % x)
        t.start()

    for x in range(5):
        t = Producer(name='生产线程%d' % x)
        t.start()

if __name__ == '__main__':
    main()