lambda_sum = lambda x,y: x + y
print(lambda_sum(3,4))

data_list = [1, 3, 5, 6]
result = map(lambda x: x+3, data_list)
r = list(result)
print(type(result))
print(r)

for i in r:
    print(i)

print("间断")

result = map(lambda x: x+3, data_list)
print(type(result))
print(list(result))

for i in list(result):
    print(i)

print(list(result))

print("间断")

result = map(lambda x: x+3, data_list)
print(type(result))

for i in list(result):
    print(i)

print(list(result))

'''
懒惰求值：只有在需要时，迭代器才会计算出具体的值。
'''