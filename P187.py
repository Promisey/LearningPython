from multiprocessing import Pool

import requests

#from P178 import decorator_timer
import time

def decorator_timer(old_function):
    def new_function(*args, **dict_arg):
        t1 = time.time()
        result = old_function(*args, **dict_arg)
        t2 = time.time()
        print("time:", t2 - t1)
        return result
    return new_function

def visit_once(i, address="http://www.cnblogs.com"):
    r = requests.get(address)
    return r.status_code

@decorator_timer
def single_thread(f, counts):
    result = map(f, range(counts))
    return list(result)


@decorator_timer
def multiple_thread(f, counts, process_number=10):
    p = Pool(process_number)
    return p.map(f, range(counts))

if __name__ == "__main__":
    TOTAL = 2
    print(single_thread(visit_once, TOTAL))
    print(multiple_thread(visit_once, TOTAL))