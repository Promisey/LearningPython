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