from math import exp, sin, cos


def f(x):
    return exp(x) * (1 + sin(x)) / (1 + cos(x))


def simpson(n):
    global a, b
    h = (b - a) / (2 * n)
    c = 1
    y_0 = f(a)
    y_2n = f(b)
    s = 0
    x = a
    for i in range(2 * n):
        x += h
        s += (3 + c) * f(x)
        c *= -1
    return h * (y_0 + y_2n + s) / 3


a = 0
b = 1.5
n = 2
s1 = simpson(n)
n *= 2
s2 = simpson(n)
while abs(s2 - s1) > 0.001:
    n *= 2
    s1 = simpson(n)
    n *= 2
    s2 = simpson(n)

print(s2)
