number_1 = '891026734517689412'  # number_1 = input('First number : ').strip()
number_2 = '75418901962345677'   # number_2 = input('Second number : ').strip()
base_pow = 4  # int(input('power base : '))


def eq_len(num, count):
    l = len(num)
    while l < count:
        num = '0' + num
        l += 1
    return num


def to_list(number):
    if base_pow >= len(number):
        raise ValueError("Power base is bigger than number length")
    number = '0' * (len(number) % base_pow) + number
    number_list = [number[i:i + base_pow] for i in range(0, len(number), base_pow)]
    number_list.append(len(number_list) - number_list.count('0' * base_pow))
    number_list.reverse()

    return number_list


def to_number(number_list):
    number_list.reverse()
    number_list.pop()
    return ''.join(number_list)


def add(number1, number2):
    if number1[0] == '-' and number2[0] == '-':
        return '-' + add(number1[1:], number2[1:])
    elif number1[0] == '-' and number2[0] != '-':
        return subtraction(number2, number1[1:])
    elif number1[0] != '-' and number2[0] == '-':
        return subtraction(number1, number2[1:])
    else:
        number1, number2 = eq_len(number1, len(number2)), eq_len(number2, len(number1))
        num1_list, num2_list = to_list(number1), to_list(number2)
        sum_list = [0]
        for i in range(1, len(num1_list)):
            sum = int(num1_list[i]) + int(num2_list[i])
            sum = str(sum)
            if len(sum) < base_pow:
                sum = '0' * (len(sum) % base_pow) + sum
            elif len(sum) > base_pow:
                if i != len(num1_list) - 1:
                    sum = sum[1:]
                    num1_list[i + 1] = str(int(num1_list[i + 1]) + 1)
            sum_list.append(sum)
    return to_number(sum_list)


def subtraction(number1, number2):
    if equal(number1, number2):
        return "0"
    elif number1[0] == '-' and number2[0] == '-':
        return subtraction(number2[1:], number1[1:])
    elif number1[0] == '-' and number2[0] != '-':
        return subtraction(number2, number1[1:])
    elif number1[0] != '-' and number2[0] == '-':
        return add(number1, number2[1:])
    elif less(number1, number2):
        return '-' + subtraction(number2, number1)
    else:
        number1, number2 = eq_len(number1, len(number2)), eq_len(number2, len(number1))
        num1_list, num2_list = to_list(number1)[1:], to_list(number2)[1:]
        subs_list = [0]
        for i in range(len(num1_list)):
            num1 = list(num1_list[i])
            num2 = list(num2_list[i])
            result = ''
            for j in range(len(num1) - 1, -1, -1):
                if num1[j] < num2[j]:
                    if j == 0:
                        l = len(num1_list[i + 1])
                        num1_list[i + 1] = str(int(num1_list[i + 1]) - 1)
                        while len(num1_list[i + 1]) < l:
                            num1_list[i + 1] = '0' + num1_list[i + 1]
                    else:
                        num1[j - 1] = str(int(num1[j - 1]) - 1)
                    num1[j] = str(int(num1[j]) + 10)
                result = str(int(num1[j]) - int(num2[j])) + result
            subs_list.append(result)
    return int(to_number(subs_list))


def equal(number1, number2):
    return to_list(number1) == to_list(number2)


def more(number1, number2):
    num1_list, num2_list = to_list(eq_len(number1, len(number2))), to_list(eq_len(number2, len(number1)))
    for i in range(len(num1_list) - 1, 1, -1):
        if num1_list[i] > num2_list[i]:
            return True
        else:
            return False


def less(number1, number2):
    return not more(number1, number2)


def more_equal(number1, number2):
    return equal(number1, number2) or more(number1, number2)


def less_equal(number1, number2):
    return less(number1, number2) or equal(number1, number2)


def division(num1, num2):
    if num2 == '0':
        raise ZeroDivisionError
    if more(num2, num1):
        return 0, int(num1)
    if equal(num1, num2):
        return 1, 0
    else:
        down = 0
        up = 10 ** base_pow
        num1 = int(num1)
        num2 = int(num2)
        while up - down != 1:
            c = num2 * ((down + up) // 2)
            if c > num1:
                up -= (up - down) // 2
            else:
                down += (up - down) // 2
    return down, subtraction(str(num1), str(down * num2))




def multiply(num1, num2):

    if num1 == '0' or num2 == '0':
        return '0'
    elif len(num2) > len(num1):
        multiply(num2, num1)
    elif num1[0] == '-' and num2[0] == '-':
        return multiply(num1[1:], num2[1:])
    elif num1[0] == '-' or num2[0] == '-':
        return '-'+str(multiply(num1[1:], num2[1:]))
    else:
        multiply_list = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num2)):
            number = '' + '0' * i
            k = 0
            for j in range(len(num2)):
                result = str(int(num2[i]) * int(num1[j]) + k)
                if j == len(num1) - 1 or len(result) == 1:
                    number = result + number
                    k = 0
                else:
                    number = result[1] + number
                    k = int(result[0])
            multiply_list.append(int(number))
    return sum(multiply_list)


def fast_multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    elif len(num2) > len(num1):
        fast_multiply(num2, num1)
    else:
        s = 0
        while int(num2)>0:
            if int(num2)%2 == 0:
                num1 = str(int(num1)*2)
                num2 = int(num2)/2
            else:
                s += int(num1)
                num2 = str(int(num2)- 1)
        return s