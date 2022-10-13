from pandas
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
    print(f"n=1")
    print(f"P({x}, {y})")
    numerator = 3 * x * x + a
    denominator = 2 * y
    print(f"s = (3*{x}^2+{a})/(2*{y})")
    if denominator == 0:
        return i
    else:
        s = slope(numerator, denominator, p)
        print(f"s = {s}")
        x_j = (s * s - 2 * x) % p
        y_j = (s * (x - x_j) - y) % p
        print(f"x = {s}^2 - 2*{x} mod {p} = {x_j}")
        print(f"y = {s}*({x}-{x_j}) - {y} mod {p} = {y_j}")
        print("n = 2")
        Q = [x_j, y_j]
        print(f"Q{Q}")
    while True:
        i += 1
        print(f"n={i}")
        numerator = Q[1] - P[1]
        denominator = Q[0] - P[0]
        print(f"s = ({Q[1]}-{P[1]})/({Q[0]}-{P[0]})")
        if denominator == 0:
            break
        else:
            s = slope(numerator, denominator, p)
            print(f"s = {s}")
            x_j = (s * s - P[0] - Q[0]) % p
            y_j = (s * (P[0] - x_j) - P[1]) % p
            print(f"x = {s}^2 - {P[0]} - {Q[0]} mod {p} = {x_j}")
            print(f"y = {s}*({x}-{x_j}) - {y} mod {p} = {y_j}")
            Q[0] = x_j
            Q[1] = y_j
            print(f"Q{Q}")
    return i


print(f"Point order: {main(0, 1, 1, 1, 3)}")
