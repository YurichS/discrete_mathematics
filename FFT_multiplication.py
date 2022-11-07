number_1 = '891026734517689412'
number_2 = '75418901962345677'
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

    return number_list


def DFT_multiply(a, b):
    a, b = eq_len(a, len(b)), eq_len(b, len(a))
    a = to_list(a)
    b = to_list(b)
    max_i = len(a) + len(b) - 2
    c_i = dict(zip(list(range(max_i + 1)), [[] for i in range(max_i + 1)]))
    for i in range(len(a)):
        for j in range(len(a)):
            c_i[i + j].append(a[i] * b[j])

    result = 0
    for i in range(max_i + 1):
        result += sum(c_i[i]) * (10 ** (base_pow * i))

    return result


print(DFT_multiply(number_1, number_2))
