import time

def decorator_timer(old_function):
    def new_function(*args, **dict_arg):
        t1 = time.time()
        result = old_function(*args, **dict_arg)
        t2 = time.time()
        print("time:", t2 - t1)
        return result
    return new_function

@decorator_timer
def add(a, b):
    return a**99+b**99
print(add(9999, 9999))