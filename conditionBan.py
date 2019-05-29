import time
import threading
import random

gMoney = 1000
gCondition = threading.Condition()
gTotalTime = 10
gTime = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            if gTime >= 10:
                gCondition.release()
                break
            gMoney += money
            print("%s生产了%d元,剩余%d元钱" % (threading.current_thread(),money,gMoney))
            gTime += 1
            gCondition.notify_all()
            gCondition.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            while gMoney < money:
                if gTime >= gTotalTime:
                    gCondition.release()
                    return
                print("%s消费者准备消费%d元钱,剩余%d元钱,不足" % (threading.current_thread(),money,gMoney))
                gCondition.wait()
            gMoney -= money
            print("%s消费了%d元钱,剩余%d元钱" % (threading.current_thread(),money,gMoney))
            gCondition.release()
            time.sleep(0.5)

def main():
    for x in range(3):
        t = Consumer(name='消费进程%d' % x)
        t.start()

    for x in range(5):
        t = Producer(name='生产进程%d' % x)
        t.start()

if __name__ == '__main__':
    main()
