matrix_size = int(input("Matrix size:"))
matrix = []
for i in range(matrix_size):
    row = []
    for j in range(matrix_size):
        row.append(0)
    matrix.append(row)

one_am = int(input("Amount of \"1\" in the matrix:"))
print("Coordinate of \"1\"")
for k in range(one_am):
    i = int(input(f"№{k}: line ="))
    j = int(input(f"№{k}: column ="))
    matrix[i][j] = 1
print("Basic matrix")
for i in range(matrix_size):
    print(matrix[i])


def trans_closure(matrix, matrix_size):
    for k in range(matrix_size):
        for i in range(matrix_size):
            if i != k and matrix[i][k] == 1:
                for j in range(matrix_size):
                    matrix[i][j] = matrix[i][j] | matrix[k][j]
    return matrix


matrix = trans_closure(matrix, matrix_size)


def simetric(matrix, matrix_size):
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] == 1:
                matrix[j][i] = 1
    return matrix


matrix = simetric(matrix, matrix_size)


def test(matrix, matrix_size):
    while True:
        if matrix == trans_closure(matrix, matrix_size):
            break
        else:
            matrix = trans_closure(matrix, matrix_size)
            matrix = simetric(matrix, matrix_size)
    return matrix


matrix = test(matrix, matrix_size)


def diagonal(matrix, matrix_size):
    for i in range(matrix_size):
        for j in range(matrix_size):
            if i == j:
                matrix[i][j] = 1
    return matrix


matrix = diagonal(matrix, matrix_size)

print("Solved matrix")
for i in range(matrix_size):
    print(matrix[i])
