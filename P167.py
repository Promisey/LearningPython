def square_sum(a, b):
    return a**2 + b**2

def cubic_sum(a, b):
    return a**3 + b**3

def argument_sum(f, a, b):
    return f(a, b)

print(argument_sum(square_sum, 3, 5))
print(argument_sum(cubic_sum, 3, 5))