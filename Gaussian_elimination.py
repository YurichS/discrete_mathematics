a = [[8.3, 3.42, 4.1, 1.9], [3.92, 8.45, 6.98, 2.46], [3.77, 8.01, 8.04, 2.28], [2.21, 2.85, 1.69, 6.99]]
b = [-9.95, 12.21, 14.85, -8.35]
length = len(a)
x = [0] * length
for col in range(length - 1):
    for row in range(col + 1, length):
        d = a[row][col] / a[col][col]
        for l_col in range(col, length):
            a[row][l_col] -= d * a[col][l_col]
        b[row] -= d * b[col]

x[length - 1] = b[length - 1] / a[length - 1][length - 1]
for i in range(length - 2, -1, -1):
    s = b[i]
    for j in range(i + 1, length):
        s -= a[i][j] * x[j]
    x[i] = s / a[i][i]

for i in range(length):
    print(f'x{i+1} = {x[i]}')
