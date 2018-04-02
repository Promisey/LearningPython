for i in (x**2 for x in range(10)):
    print(i)

print("间断")

for i in [x**2 for x in range(10)]:
    print(i)

print("间断")

r = [x**2 for x in range(10)]
print(r)

print("间断")

a = range(100000000)
result = map(lambda x: x**2, a)
print(list(result))