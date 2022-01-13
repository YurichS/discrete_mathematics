import numpy as np

print("a^x=b(mod m)")
a = int(input("a="))
b = int(input("b="))
m = int(input("m="))

s = [2, 3, 5, 7]
coefficients = []
results = []


def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def factorization(t):
    equation = []
    count = 0
    for i in s:
        power = 0
        while True:
            if t % i == 0:
                t = t / i
                power += 1
                count += 1
            else:
                break
        equation.append(power)
    if count > 1:
        coefficients.append(equation)
        return True
    else:
        return False


if gcd(a, m) == gcd(b, m) == 1:
    for k in range(0, m):
        c = (a ** k) % m
        if factorization(c):
            results.append(k)
        if len(results) == 4:
            break
    logs = np.linalg.solve(np.array(coefficients), np.array(results))
    logs_list = logs.astype(int)
    coefficients = []
    for K in range(0, m):
        if factorization((b * a ** K) % m):
            sum = 0
            for i in range(4):
                sum += coefficients[0][i] * logs_list[i]
            break
    x = (sum - K) % m
    print(f"x={x}")
else:
    print("Numbers are not coprime")
