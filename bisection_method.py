def f(x):
    return x ** 3 - x ** 2 + 3


def bisection_method(a, b, error):
    while abs(b - a) > error:
        x = (a + b) / 2
        if f(x) == 0:
            break
        else:
            if f(a) * f(x) > 0:
                a = x
            else:
                b = x
    return x


print(bisection_method(-2, -1, 10 ** (-4)))
