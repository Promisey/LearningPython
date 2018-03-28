class Bird(object):
    feather = True

class Chincken(Bird):
    fly = False
    def __init__(self, age):
        self.age = age

    def get_adult(self):
        if self.age > 1.0:
            return True
        else:
            return False
    adult = property(get_adult)

summer = Chincken(2)
print(summer.adult)

summer.age = 0.5
print(summer.adult)

class num(object):
    def __init__(self,value):
        self.value = value

    def get_neg(self):
        return -self.value

    def ss(self,value):
        self.value = -value

    def del_neg(self):
        print("value also deleted")
        del self.value

    neg = property(get_neg, ss, del_neg, "I'm negative")

x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg