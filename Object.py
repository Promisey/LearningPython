# coding=utf-8
'''
class bird(object):
    # def chirp(self, sound):
        # print(sound)
    # def set_color(self, color):
        # self.color = color
    def __init__(self, color):
        self.color = color
        print("my color is", color)
    def ca(self):
        print(self.color)
"""
    def __init__(self, sound):
        self.sound = sound
        print("my sound is:", sound)
    def chirp(self):
        print(self.sound)
"""
summer = bird("yellow")
# summer.chirp("ji")
# summer.set_color("yellow")
# print(summer.color)
summer.ca()
# summer.chirp()
# summer = bird()
# summer.set_color("yellow")
# print(summer.color)

print()

class bird(object):
    def chirp(self, sound):
        print(sound)

    def chirp_repeat(self, sound, n):
        for i in range(n):
            self.chirp(sound)
summer = bird()
summer.chirp_repeat("ji",10)
'''

a = [1,2,3]
print(dir(a))

b = (1.8).__mul__(2.0)
print(b)

c = True.__or__(False)
print(c)

class SuperList(list):
    def __sub__(self,b):
        a = self[:]
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print(SuperList([1,2,3]) - SuperList([3,4]))


d = [1,2]
print(d[1])
print(d.__getitem__(1))

li = [1,2,3,4,5,6]
li.__setitem__(3,0)
print(li)

example_dict = {"a":1,"b":2}
example_dict.__delitem__("a")
print(example_dict)

print(len([1,2,3]))
print([1,2,3].__len__())

print((-1).__abs__())
print((2.3).__int__())

# 属性
class Bird(object):
    feather = True

    def chirp(self):
        print("some sound")

class Chicken(Bird):
    fly = False

    def __init__(self, age):
        self.age = age

    def chirp(self):
        print("ji")

summer = Chicken(2)
print("===> summer")
print(summer.__dict__)

print("===> Chicken")
print(Chicken.__dict__)

print("===> Bird")
print(Bird.__dict__)

print("===> object")
print(object.__dict__)

print("summer 的全部属性")
print(dir(summer))


autumn = Chicken(3)
autumn.feather = False
print(summer.feather)
print(dir(autumn))