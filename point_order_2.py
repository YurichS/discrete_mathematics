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


def main(x, y, a, b, p):
    i = 2
    P = (x, y)
    numerator = 3 * x * x + a
    denominator = 2 * y
    if denominator == 0:
        return i
    else:
        s = slope(numerator, denominator, p)
        x_j = (s * s - 2 * x) % p
        y_j = (s * (x - x_j) - y) % p
        Q = [x_j, y_j]
    while True:
        numerator = Q[1] - P[1]
        denominator = Q[0] - P[0]
        i += 1
        if denominator == 0:
            break
        else:
            s = slope(numerator, denominator, p)
            Q[0] = (s * s - P[0] - Q[0]) % p
            Q[1] = (s * (P[0] - Q[0]) - P[1]) % p
    return i


print(main(2, 2, 1, 1, 7))
