from P178 import decorator_timer

def decorator_class(SomeClass):
    class NewClass(object):
        def __init__(self, age):
            self.total_dispaly = 0
            self.wrapped = SomeClass(age)
        def display(self):
            self.total_dispaly += 1
            print("total display", self.total_dispaly)
            self.wrapped.display()
    return NewClass

@decorator_timer
@decorator_class
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("my age is", self.age)

if __name__ == "__main__":
    eagle_lord = Bird(5)
    for i in range(3):
        eagle_lord.display()
