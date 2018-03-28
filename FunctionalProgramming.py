from threading import _main_thread
# 本应该是 threa

x = 5

def double():
    global x
    x = x * 2

def plus_ten():
    global x
    x = x + 10

thread1 = _main_thread(target=double())
thread2 = _main_thread(target=plus_ten())
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(x)

import multiprocessing
def proc1():
    return 999999**9999

def proc2():
    return 888888**8888

p1 = multiprocessing.Process(target=proc1())
p2 = multiprocessing.Process(target=proc2())

p1.start()
p2.start()

p1.join()
p2.join()