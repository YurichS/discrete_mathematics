#  Runge–Kutta 3 order autostep
# Імпорт бібліотек
from matplotlib.pyplot import plot, show

# Кількість рівнянь в системі
n = 3
# Масив в якому будуть зберігатись значння коефіцієнтів к
k = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Задання проміжку
x_0 = 0
x_n = 1.5
# Задання похибки
error = 0.001
# Початкові значення рівнянь системи в точці х_0
y_n = [0, 0, 0]
# Масиви для збереження значень Х та У для побудови графіка
y_gr = [0]
x_gr = [0]


# Реалізація системи рівнянь з заданими коефіцієнтами
def f(y1, y2, y3):
    Tm = 0.003
    T1 = 0.3
    T2 = 0.02
    C = 3
    Ke = 15
    Ku = 2
    K1 = 1.01
    K2 = 1
    dy1 = (-y3 + Ke * Ku * (K1 - K2 * y2) - (T1 + T2) * y1) / (T1 * T2)
    dy2 = (C * y3 - y2) / Tm
    dy3 = y1
    return dy1, dy2, dy3


# Реалізація методу Рунге-Кутта 3ого порядку

def RK3(h, y):
    y = y[:]
    x = x_0
    for i in range(n):
        k[i][0] = h * f(y[0], y[1], y[2])[i]
    x += h / 2
    for i in range(n):
        k[i][1] = h * f(y[0] + k[0][0] / 2, y[1] + k[1][0] / 2, y[2] + k[2][0] / 2)[i]
    x += h / 2
    for i in range(n):
        k[i][2] = h * f(y[0] - k[0][0] + 2 * k[0][1], y[1] - k[1][0] + 2 * k[1][1], y[2] - k[2][0] + 2 * k[2][1])[i]
    for i in range(n):
        y[i] += (k[i][0] + 4 * k[i][1] + k[i][2]) / 6
    return y


def RK3_main():
    global x_0, y_n
    # Оголошення початкового значення кроку
    h1 = (x_n - x_0) / 1000
    # Реалізація автоматичної зміни кроку
    K = 0
    while x_0 < x_n:
        y1 = RK3(h1, y_n)
        h2 = h1 / 2
        y2 = RK3(h2, y_n)
        y2 = RK3(h2, y2)
        if abs(y2[1] - y1[1]) < error:
            x_0 += h1
            y_n = y2[:]
            y_gr.append(y_n[1])
            x_gr.append(x_0)
            if K == 0:
                h1 *= 2
        else:
            h1 /= 2
            K = 1
    return x_gr, y_gr


x_gr, y_gr = RK3_main()
# Вивід отриманого графіка
plot(x_gr, y_gr)
show()
