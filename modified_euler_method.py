# modified Euler method for ODE with autostep
import matplotlib.pyplot as plt

n = 3  # кілкість рівнянь системи
x0 = 0  # початок проміжку
xn = 4  # кінець проміжку
e = 0.001  # похибка
y = [0, 0, 0]  # початкові значення функції
# масиви для зберігання значень для графіка
y_plot = [0]
t_plot = [0]


# реалізація системи рівнянь
def f(y1, y2, y3):
    O_m = 4
    U_s = 0.1
    C_u = 8 * 10 ** (-5)
    C_w = 3 * 10 ** (-5)
    I_D = 0.03 * 10 ** (-5)
    I_N = 2 * 10 ** (-5)
    K_M = 10
    T = 0.02
    i = 30
    K_p = 300
    I = I_D + I_N / (i ** 2)
    dy1 = (K_M * U_s * (1 - y2)) / (T * O_m) - (y1 / T)
    dy2 = y3 / i
    dy3 = (C_u * K_p * y1 - C_w * y3) / I
    return dy1, dy2, dy3


# Класичний метод Ейлера
def Euler(h, y_n):
    y_n = y_n.copy()
    for i in range(n):
        y_n[i] += h * f(y_n[0], y_n[1], y_n[2])[i]
    return y_n


# Модифікований метод Ейлера
def Modified_Euler(h, y_n, y_e):
    y_n = y_n.copy()
    for i in range(n):
        y_n[i] += 0.5 * h * (f(y_n[0], y_n[1], y_n[2])[i] + f(y_e[0], y_e[1], y_e[2])[i])
    return y_n


# реалізація автокроку
h1 = (xn - x0) / 1000  # початкове значення кроку
K = 0  # ознака поділу кроку
while x0 < xn:
    ye_1 = Euler(h1, y)
    y_1 = Modified_Euler(h1, y, ye_1)
    h2 = h1 / 2
    ye_21 = Euler(h2, y)
    y_21 = Modified_Euler(h2, y, ye_21)
    ye_22 = Euler(h2, ye_1)
    y_22 = Modified_Euler(h2, y_21, ye_22)
    if abs(y_22[1] - y_1[1]) < e:
        y = y_22.copy()
        x0 += h1
        t_plot.append(x0)
        y_plot.append(y_22[1])
        if K == 0:
            h1 *= 2
    else:
        K = 1
        h1 /= 2


def MME():
    print(f'ММЕ - {len(t_plot)}')
    return t_plot, y_plot


# виведення графіка
plt.xlabel('t')
plt.ylabel('y2(t)')
plt.plot(t_plot, y_plot, label='MME')
plt.title("Модифікований метод Ейлера")
plt.legend(loc='lower right')
plt.show()
print("№  | t | y2(t)")
for i in range(len(t_plot)):
    if i % 20 == 0:
        print(f"{i}  | {t_plot[i]}  | {y_plot[i]}")
