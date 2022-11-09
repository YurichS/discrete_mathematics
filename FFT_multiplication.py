from sympy import cos, sin, pi, I, simplify

number_1 = '8910267345176894'
number_2 = '7541890196234567'
base_pow = 4


def eq_len(num, count):
    l = len(num)
    while l < count:
        num = '0' + num
        l += 1
    return num


def to_list(number):
    if base_pow >= len(number):
        raise ValueError("Power base is bigger than number length")
    l = len(number) % base_pow
    if l == 1:
        number = '0' * (base_pow - 1) + number
    else:
        number = '0' * l + number
    number_list = [int(number[i:i + base_pow]) for i in range(0, len(number), base_pow)]
    number_list.reverse()
    return number_list + [0] * len(number_list)


def vandermonde_matrix(n):
    w = cos(2 * pi / n) + sin(2 * pi / n) * I
    matrix = [[1] * n]
    for i in range(1, n):
        line = []
        for k in range(n):
            line.append((w ** (k * i)))
        matrix.append(line)

    return matrix


def matrix_multiplication(matrix_1, matrix_2):
    l = len(matrix_2)
    result = [0 for i in range(l)]
    for i in range(l):
        for j in range(l):
            result[i] += matrix_1[i][j] * matrix_2[j]
    return result


def inverse_vandermonde_matrix(n):
    matrix = vandermonde_matrix(n)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = 1 / matrix[i][j]
    return matrix

def FFT_multiplication(number1, number2):
    number1, number2 = eq_len(number1, len(number2)), eq_len(number2, len(number1))
    number1 = to_list(number1)
    number2 = to_list(number2)
    n = len(number1)
    vandermondeMatrix = vandermonde_matrix(n)
    dft_matrix1 = matrix_multiplication(vandermondeMatrix, number1)
    dft_matrix2 = matrix_multiplication(vandermondeMatrix, number2)
    dft_matrix = [dft_matrix1[i]*dft_matrix2[i] for i in range(n) ]
    inverse_vandermondeMatrix = inverse_vandermonde_matrix(n)
    matrix = matrix_multiplication(inverse_vandermondeMatrix, dft_matrix)
    matrix = [i/n for i in matrix]
    s = 0
    for i in range(n):
        s += int(matrix[i].simplify()) * (10 ** (base_pow*i))
    return s

print(int(FFT_multiplication(number_1, number_2)))
print(int(number_1)*int(number_2))
