from math import exp


def f(x):
    return exp(2 * x) - exp(x) + 1


def trapezoidal(a, b, error):
    n = b
    x = a
    h = (b - a) / n
    s1 = 0
    s = 0
    while a != b:
        s += (f(a) + f(a + h)) * h / 2
        a += h
    while abs(s - s1) > error:
        a = x
        s1 = s
        s = 0
        n *= 2
        h = (b - a) / n
        while a != b:
            s += (f(a) + f(a + h)) * h / 2
            a += h
    return s


print("Корінь рівняння:", trapezoidal(0, 2, 0.001))
