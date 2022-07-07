# Runge-Kutta-Merson method for ODE solve with autostep
import matplotlib.pyplot as plt

n = 4

x0 = 0
xn = 5

e = 0.001
k1 = [0, 0, 0, 0]
k2 = [0, 0, 0, 0]
k3 = [0, 0, 0, 0]
k4 = [0, 0, 0, 0]
k5 = [0, 0, 0, 0]
R = [0, 0, 0, 0]
y = [0, 0, 0, 0]

y_plt = [0]
t_plt = [0]


def f(y1, y2, y3, y4):
    T_m = 0.05
    T_k = 0.02
    T_1 = 0.004
    C = 10
    i = 200
    K1 = 2
    K2 = 2
    Kp = 3
    S = 60
    dy1 = (K1 * Kp * S * (1 - y2) - y1) / T_1
    dy2 = y4 / i
    dy3 = ((K2 * y1) - y3) / T_k
    dy4 = ((C * y3) - y4) / T_m
    return dy1, dy2, dy3, dy4


def method(h, yn):
    global R
    yn = yn[:]
    for i in range(n):
        k1[i] = h * f(yn[0], yn[1], yn[2], yn[3])[i]
    for i in range(n):
        k2[i] = h * f(yn[0] + k1[0] / 3, yn[1] + k1[1] / 3, yn[2] + k1[2] / 3, yn[3] + k1[3] / 3)[i]
    for i in range(n):
        k3[i] = h * f(yn[0] + (k1[0] + k2[0]) / 6, yn[1] + (k1[1] + k2[1]) / 6, yn[2] + (k1[2] + k2[2]) / 6,
                      yn[3] + (k1[3] + k2[3]) / 6)[i]
    for i in range(n):
        k4[i] = h * f(yn[0] + (k1[0] + 3 * k3[0]) / 8, yn[1] + (k1[1] + 3 * k3[1]) / 8, yn[2] + (k1[2] + 3 * k3[2]) / 8,
                      yn[3] + (k1[3] + 3 * k3[3]) / 8)[i]
    for i in range(n):
        k5[i] = h * f(yn[0] + 2 * k3[0] + (k1[0] - 3 * k3[0]) / 2, yn[1] + 2 * k3[1] + (k1[1] - 3 * k3[1]) / 2,
                      yn[2] + 2 * k3[2] + (k1[2] - 3 * k3[2]) / 2, yn[3] + 2 * k3[3] + (k1[3] - 3 * k3[3]) / 2)[i]
    for i in range(n):
        yn[i] += (k1[i] + 4 * k4[i] + k5[i]) / 6
        R[i] = (-2 * k1[i] + 9 * k3[i] - 8 * k4[i] + k1[i]) / 30
    return yn


h = (xn - x0) / 1000
while x0 < xn:
    y_n = method(h, y)
    if abs(R[1]) > e:
        h /= 2
    else:
        if abs(R[1]) < (e / 30):
            h *= 2
        else:
            y = y_n[:]
            x0 += h
            y_plt.append(y[1])
            t_plt.append(x0)

plt.xlabel('t')
plt.ylabel('y2(t)')
plt.plot(t_plt, y_plt)
plt.show()
print(len(t_plt))
print("t  | y2(t)")
for i in range(len(t_plt)):
    if i % 15 == 0:
        print(f"{t_plt[i]}  | {y_plt[i]}")
