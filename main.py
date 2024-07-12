import re

user_name = input("Введите имя: ")

name_pattern = r'^[A-Za-zА-Яа-я]+$'

if re.match(name_pattern, user_name):
    if user_name == "Денис":
        print("Нет Денисам!")
    elif user_name == ("Денис".lower()):
        print("Нет Денисам!")
    else:
        while True:
            op = input("какая операшн? ")
            if op == "1":
                a = int(input("введите первое число: "))
                b = int(input("Введите второе число: "))
                print("Результат:", a + b)
            elif op == "2":
                a = int(input("введите первое число: "))
                b = int(input("Введите второе число: "))
                print("Результат:", a - b)
            elif op == "3":
                a = int(input("введите первое число: "))
                b = int(input("Введите второе число: "))
                print("Результат:", a * b)
            elif op == "4":
                a = int(input("введите первое число: "))
                b = int(input("Введите второе число: "))
                print("Результат:", a / b)
            elif op == "one":
                a = int(input("Введите наименьшее число диапазона: "))
                b = int(input('введите наибольшее число диапазона: '))
                sum_ = 0
                for i in range(a,b+1):
                    sum_ += i
                print(sum_)
            elif op == "!":
                a = int(input("введите n: "))
                quantity = 1
                for i in range(1, a+1):
                    quantity *= i
                print(quantity)
            elif op == "*":
                a = int(input("Введи 1: "))
                b = int(input("Введи 2: "))
                for i in range(1, b + 1):
                    print(f"{a}*{i}=", a * i)

            elif op == '0':
                break
            else:
                print("error")
                break
else:
    print("Имя содержит недопустимые символы.")