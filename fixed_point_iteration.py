# x*x + sin(2x) - 2
# eps = 0.0001
# [-1.5, -1.4]

from math import sqrt, fabs

def f(x):
    return sqrt(2-math.sin(2*x))

def simple_iter(a, b, eps):
    counter = 0;
    x = (a + b) / 2
    z = x
    x = f(x)
    while fabs(x - z) >= eps:
        z = x
        x = f(x)
        print(counter, x)
        counter += 1

simple_iter(-1.5, -1.4, 0.0001)