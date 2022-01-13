number = int(input("Number:"))
mod = int(input("Module:"))


def GetModReverse(number, mod):
    if number % mod == 0:
        print("Reversed number doesn\'t exist")
    else:
        i = 0
        while (mod * i + 1) % number != 0:
            res = (mod * (i + 1) + 1) / number
            i += 1
            print(f"{i-1} - {res}")
        return res


print(GetModReverse(number, mod))
