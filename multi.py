
def multi(num):
    num1 = 1
    while num1 <= num:
        print(f"{num1} x {num} = {num*num1}")
        num1 += 1

num = int(input('Введите число: '))
multi(num)
