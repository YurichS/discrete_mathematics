# Euler method for ODE solve
from matplotlib.pyplot import plot, show

n = 3
x0 = 0
xn = 5
y = [0, 0, 0]
y_gr = [0]
x_gr = [0]
e = 0.001


def f(y1, y2, y3):
    i = 30
    O_m = 4
    U_s = 0.3
    C_u = 7 * 10 ** (-5)
    C_w = 1.5 * 10 ** (-5)
    I_D = 0.03 * 10 ** (-5)
    I_N = 1 * 10 ** (-5)
    k = 0.1
    T = 0.02
    K_p = 2000
    I = I_D + I_N / i ** 2

    dy1 = y3 / i
    dy2 = (U_s * (1 - y1) / (O_m * T)) - (y2 / (k * T)) - (U_s * y3 / (O_m * i))
    dy3 = (C_u * K_p * y2 - C_w * y3) / I

    return dy1, dy2, dy3


def Euler(h, y_n):
    y_n = y_n.copy()
    for i in range(n):
        y_n[i] += h * f(y_n[0], y_n[1], y_n[2])[i]
    return y_n


h1 = 0.0005
while x0 < xn:
    y = Euler(h1, y)
    y_gr.append(y[0])
    x0 += h1
    x_gr.append(x0)

plot(x_gr, y_gr)
show()

