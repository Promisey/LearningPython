a = 1
print(id(1))
print(id(a))

def f(x):
    print(id(x))
    x = 100
    print(id(x))

a = 1
print(id(a))

f(a)
print(a)
print(id(100))