from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))
b = a
print(getrefcount(b))

class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj

b = [1, 2, 3]
print(id(b))
a = from_obj(b)
print(id(a.to_obj))

a = [1]
print(getrefcount(a))
b = [a, a]
print(getrefcount(b))
print(getrefcount(a))

x = [1, 2, 3]
y = [x, dict(key1=x)]
z = [y, (x, y)]

import objgraph
objgraph.show_refs([z], filename="ref_topo.png")
# 没有dot

m = [1, 2, 3]
n = m
o = n
p = o
print(getrefcount(n))
print(getrefcount(o))