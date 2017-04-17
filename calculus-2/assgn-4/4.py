from math import factorial

def d1(x, y):  # first derivative
    return 3 * x * y

def d2(x, y):  # second derivative
    return 3 * x * d1(x, y) + 3 * y

def d3(x, y):  # third derivative
    return 6 * d1(x, y) + 3 * x * d2(x, y)

terms = [d1, d2, d3]
initial_condition = 0.5
step = 0.1

def x(i):
    return step * i

def h(i):
    return pow(step, i) / factorial(i)

def euler(i, n, d):
    return h(n) * d(x(i), y(i))

def y(i_1):  # i_1 means i + 1
    if i_1 == 0:
        return initial_condition
    i = i_1 - 1
    return y(i) + sum([
        euler(i, n + 1, d) for n, d in enumerate(terms)
    ])

array_fmt = "{0} & {1} & {2:.6f} \\\\"
for i in range(0, 5):
    print(array_fmt.format(i, x(i), y(i)))
