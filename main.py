
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
# import re
#
# user_name = input("Введите имя: ")
#
# name_pattern = r'^[A-Za-zА-Яа-я]+$'
#
# if re.match(name_pattern, user_name):
#     if user_name == "Денис":
#         print("Нет Денисам!")
#     elif user_name == ("Денис".lower()):
#         print("Нет Денисам!")
#     else:
#         while True:
#             op = input("какая операшн? ")
#             if op == "1":
#                 a = int(input("введите первое число: "))
#                 b = int(input("Введите второе число: "))
#                 print("Результат:", a + b)
#             elif op == "2":
#                 a = int(input("введите первое число: "))
#                 b = int(input("Введите второе число: "))
#                 print("Результат:", a - b)
#             elif op == "3":
#                 a = int(input("введите первое число: "))
#                 b = int(input("Введите второе число: "))
#                 print("Результат:", a * b)
#             elif op == "4":
#                 a = int(input("введите первое число: "))
#                 b = int(input("Введите второе число: "))
#                 print("Результат:", a / b)
#             elif op == "one":
#                 a = int(input("Введите наименьшее число диапазона: "))
#                 b = int(input('введите наибольшее число диапазона: '))
#                 sum_ = 0
#                 for i in range(a,b+1):
#                     sum_ += i
#                 print(sum_)
#             elif op == "!":
#                 a = int(input("введите n: "))
#                 quantity = 1
#                 for i in range(1, a+1):
#                     quantity *= i
#                 print(quantity)
#             elif op == "*":
#                 a = int(input("Введи 1: "))
#                 b = int(input("Введи 2: "))
#                 for i in range(1, b + 1):
#                     print(f"{a}*{i}=", a * i)
#
#             elif op == '0':
#                 break
#             else:
#                 print("error")
#                 break
# else:
#     print("Имя содержит недопустимые символы.")


# Угадайка
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



# Справка
# .append() - добавление в конец
# .pop() - удаление по индексу
# .remove() - удаление по значению
# .insert(через запятую, сначала индекс, а потом значение) - вставка



# Списки и ху
# spis = [6, 5, 10, -4, -5]
# minn = float("inf")
# for num in spis:
#     if num < minn:
#         minn = num
# print(minn)


# 1. Среднее арифметическое
# import statistics
#
# spiska = [-14, 37, 48, 27, -52, 0, 83, 93, -1]
#
# # srednee = sum(spiska) / len(spiska)
# # print(srednee)
#
# srednee = statistics.mean(spiska)
#
# print(srednee)

# 2. Кол-во в диапазоне
# k = 0
# for num in range(2077, 105793+1):
#     if(num % 3 == 0 and  num % 7 == 0 and num % 11 != 0 and num % 5 != 0):
#         k+=1
# print (k)

# 4. Число в столбик
# spisok = [13, -7, 32,57,31,-9,0]
# for num in spisok:
#     num *= 10
#     print(num)

# 5. Ну типа сделал список хз
# sp = []
# while True:
#     a = int(input("число: "))
#     sp.insert(0, a)
#     if a <= 0:
#         break
# print (sp)


# N = int(input())
# k = 0
# for i in range(N):
#     num = int(input())
#     if (num % 2 != 0):
#         k+=1
# print(k)

# def count_odd(spis: list):
#     k = 0
#     for i in spis:
#         if (i % 2 != 0):
#             k+=1
#     print(k)
#
# chisla = [1,4,6,7,3]
# count_odd(chisla)

# def count_AB(string: str):
#     k = 0
#     for i in range(len(string)):
#         print(i)
# count_AB("ABABAB")





# 1ифелсе

# a = int(input("Введите число: "))
# if a % 2==0:
#     print("четное")
# else:
#     print("нечетное")

# 2
# a = int(input("Введите число: "))
# if a < 0:
#     print("число меньше нуля")
# elif a > 0:
#     print("число больше нуля")
# else:
#     print("число равно нулю")

# 3
# score = int(input("Введите число: "))
# if 90 <= score <= 100:
#     print("A")
# if 80 <= score < 90:
#     print("B")
# if 70 <= score < 80:
#     print("C")
# if 60 <= score < 70:
#     print("D")
# if 0 <= score < 60:
#     print("F")

# 4
# year = int(input("Введите год: "))
# if year % 4 == 0:
#     print("Этот год високосный.")
# else:
#     print("Этот год не является високосным.")

# 5
# try:
#     frst_num = float(input("Введите первое число: "))
#     sec_num = float(input("Введите второе число: "))
#     if frst_num > sec_num:
#         print("Первое число больше")
#     elif frst_num < sec_num:
#         print("Второе число больше")
#     else:
#         print("Числа равны")
# except:
#     print("Пока пользователь!")


# 1 cicle
user_num = int(input("Введите количество билетов: "))
kolvo_tic = 0
for i in range(user_num):
    user_input = (input("Введите номер билета: "))
    while len(user_input) != 6:
        user_input = (input("Введите номер билета (6 символов): "))
    a = int(user_input[0]) + int(user_input[1]) + int(user_input[2])
    b = int(user_input[3]) + int(user_input[4]) + int(user_input[5])
    if a == b:
        print("Билет счастливый! ")
        kolvo_tic += 1
    else:
        print("Билет несчастливый! ")
print("Количетсво счастливых билетов -", kolvo_tic)
        # if user_input[0] + user_input[1] + user_input[2] == user_input[3] + user_input[4] + user_input[5]: