a = [[3.92, 8.45, -0.98, 1.4],
     [3.3, 13.42, 4.1, 1.9],
     [3.77, 2.01, 8.04, 0.28],
     [2.21, 2.85, 1.69, 9.99]]
b = [12.21, -9.95, 14.85, -8.35]
l = len(a)
x = b[:]  # Початкові наближення


# Перевірка на діагональну перевагу
def diagonal_pr(a, l):
    for col in range(l):
        s = 0
        for row in range(l):
            if row != col:
                s += a[col][row]
        if 2 * a[col][col] <= s:
            return False
    return True


# Ітераційний процес
def iterations():
    global x
    for row in range(l):
        s = 0
        for col in range(l):
            if col != row:
                s += a[row][col] / a[row][row] * x[col]
        x[row] = b[row] / a[row][row] - s


if diagonal_pr(a, l):
    print('Діагональна перевага виконується')
else:
    print('Діагональна перевага не виконується')
for _ in range(40):
    iterations()
for i in range(l):
    print(f'x{i + 1} = {x[i]}')
