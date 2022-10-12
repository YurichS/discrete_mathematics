from math import ceil, sqrt


def mod_reverse(number, module):
    for i in range(1000):
        if number * i % module == 1:
            return i
    return "Don't exists"


def slope(numerator, denominator, p):
    if numerator % denominator != 0:
        if numerator < 0 and denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        denominator = mod_reverse(denominator, p)
        s = (numerator * denominator) % p
    else:
        s = (numerator / denominator) % p
    return s


def even_point(x, y, a, b, p):
    numerator = 3 * x * x + a
    denominator = 2 * y
    s = slope(numerator, denominator, p)
    x_j = (s * s - 2 * x) % p
    y_j = (s * (x - x_j) - y) % p
    return x_j, y_j


def odd_point(x1, y1, x2, y2, p):
    numerator = y2 - y1
    denominator = x2 - x1
    s = slope(numerator, denominator, p)
    x_j = (s * s - x1 - x2) % p
    y_j = (s * (x1 - x_j) - y1) % p
    return x_j, y_j


def point_order(x, y, a, b, p):
    m = ceil(sqrt(p + 1 + 2 * sqrt(p)))
    P = [(x, y)]
    for j in range(1, m):
        if j % 2 != 0:
            P.append(even_point(P[j // 2][0], P[j // 2][1], a, b, p))
        else:
            P.append(odd_point(P[j - 1][0], P[j - 1][1], P[0][0], P[0][1], p))
    alpha = (P[m - 1][0] % p, (-1 * P[m - 1][1]) % p)
    i = 1
    q = alpha
    while q not in P:
        if q[0] != alpha[0]:
            q = odd_point(q[0], q[1], alpha[0], alpha[1], p)
        else:
            q = even_point(q[0], q[1], a, b, p)
        i += 1
    n = m * i + P.index(q) + 1
    return n


print(point_order(0, 1, 3, 1, 7))
