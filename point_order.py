from math import ceil, sqrt


def mod_reverse(number, module):
    for i in range(1000):
        if number * i % module == 1:
            return i
    return "Don't exists"


def point_order(x, y, a, b, p):
    m = ceil(sqrt(p + 1 + 2 * sqrt(p))) + 1
    P = [(x, y)]
    for j in range(2, m):
        if j % 2 == 0:
            numerator = 3 * x * x + a
            denominator = 2 * y
        else:
            numerator = P[0][1] - P[j - 1][1]
            denominator = P[0][0] - P[j - 1][0]
        if not numerator % denominator:
            if numerator < 0 and denominator < 0:
                numerator = abs(numerator)
                denominator = abs(denominator)
            denominator = mod_reverse(denominator, p)
            s = (numerator * denominator) % p
        else:
            s = (numerator / denominator) % p
