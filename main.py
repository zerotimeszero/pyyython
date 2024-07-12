
# if op == 1:
#     print("Результат:", c + d)
# elif op == 2:
#     print("Результат:", c - d)
# elif op == 3:
#     print("Результат:", c * d)
# elif op == 4:
#     print("Результат:", c / d)
# else:
#     print("Такой операции нет, до свидания!")
# i=1
# for i in range(1+1,100+1):
#     # print("|-|")
#     print(i)
import re

# Запрашиваем у пользователя ввод имени
user_name = input("Введите имя: ")

# Определяем шаблон для проверки имени (только буквы)
name_pattern = r'^[A-Za-zА-Яа-я]+$'

# Проверяем, соответствует ли введенное имя шаблону
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

# a=int(input("загадайте число"))


# while True:
#     b = int(input("угадайте число"))
#     if b < a:
#         print("menshe")
#         if b == 10:
#             break
#     elif b > a:
#         print("bolsche")
#     else:
#         print("pobeda")
#         break

# for i in range(1,10+1):
#     if i == 3:
#         break
#     print("hui")




# .append() - добавление в конец
# .pop() - удаление по индексу
# .remove() - удаление по значению
# .insert(через запятую, сначала индекс, а потом значение) - вставка




# spis = [6, 5, 10, -4]
# product = 1
# for number in spis:
#     product *= number
#
# print("Произведение всех чисел в списке:", product)