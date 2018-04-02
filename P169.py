def line_conf():
    def line(x):
        return 2*x+1
    return line
'''
my_line = line_conf()
print(my_line(5))
'''

if __name__=="main":
    line_conf()
    print(line(5))