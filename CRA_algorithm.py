c_am = int(input("Amount of congruence relation:"))
a = []
m = []
for i in range(c_am):
    a_i = int(input(f"a{i + 1}="))
    a.append(a_i)
    m_i = int(input(f"m{i + 1}="))
    m.append(m_i)
print("Coprime integers check")


def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


gcd_tst = True
for i in range(c_am - 1):
    if gcd(m[i], m[i + 1]) == 1:
        print(f"GCD({m[i]}, {m[i + 1]})=1")
    else:
        print(f"GCD({m[i]}, {m[i + 1]})!=1")
        gcd_tst = False
        break

if gcd_tst:
    M_gen = 1
    for i in m:
        M_gen = M_gen * i
    M = [M_gen / i for i in m]
    Y = []
    for i in range(c_am):
        y = 1
        while True:
            if (M[i] * y) % m[i] == a[i]:
                Y.append(y)
                break
            else:
                y += 1
    x = lambda m1, m2: sum([m1[i] * m2[i] for i in range(c_am)]) % M_gen
    print(f"x ≡ {x(M, Y)}(mod {M_gen})")
