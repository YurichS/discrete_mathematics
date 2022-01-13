from random import randrange
from math import gcd

n = int(input("n="))


def random_param(n):
    x_rand, y_rand, a_rand = randrange(n), randrange(n), randrange(n)
    return x_rand, y_rand, a_rand


while True:
    x, y, a = random_param(n)
    b = (y ** 2 - x ** 3 - a * x) % n
    g = gcd(n, 4 * (a ** 3) + 27 * (b ** 2))
    if 1 < g < n:
        print(f"{n}={g}*{int(n / g)}")
        break

