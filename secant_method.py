# e = 10**(-4)
# x*x - cos(x) = 0
# [0.7;0.8]

from math import cos


def f(x):
    return x * x - cos(x)


def secant_method(x_n, x_f, e):
    r = f(x_f)
    x_0 = x_n - (f(x_n) * (x_n - x_f)) / (f(x_n) - r)
    while abs(x_0 - x_n) > e:
        x_n = x_0
        x_0 = x_n - (f(x_n) * (x_n - x_f)) / (f(x_n) - r)
    return x_0


print(secant_method(0.8, 0.7, 0.0001))
