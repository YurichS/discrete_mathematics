from math import sqrt

print("a^x = b (mod p)")
a = int(input("a="))
b = int(input("b="))
p = int(input("p="))

H = round(sqrt(p)) + 1
c = (a ** H) % p
answer_exist_check = False
for u in range(1, H + 1):
    for v in range(H + 1):
        if (c ** u) % p == (b * a ** v) % p:
            print(f"u={u}, v={v} => x={H * u - v}")
            answer_exist_check = True
            break
if not answer_exist_check:
    print("answer doesn't exist")
