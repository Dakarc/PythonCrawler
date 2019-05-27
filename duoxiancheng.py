import time
import threading

def coding():
    for x in range(3):
        print('正在写代码%s'%x)
        time.sleep(1)

def drawing():
    for x in range(3):
        print('正在画图%s'%x)
        time.sleep(1)

def main():
    # coding()
    # drawing()
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()