
# 1 cicle
# user_num = int(input("Введите количество билетов: "))
# kolvo_tic = 0
# for i in range(user_num):
#     user_input = (input("Введите номер билета: "))
#     while len(user_input) != 6:
#         user_input = (input("Введите номер билета (6 символов): "))
#     a = int(user_input[0]) + int(user_input[1]) + int(user_input[2])
#     b = int(user_input[3]) + int(user_input[4]) + int(user_input[5])
#     if a == b:
#         print("Билет счастливый! ")
#         kolvo_tic += 1
#     else:
#         print("Билет несчастливый! ")
# print("Количетсво счастливых билетов -", kolvo_tic)

# 2
# N = int(input())
# for i in range(N, 0, -1):
#     print (i)
# print("Бомбаа взорвалась!")

# 3
# num = int(input("Введите число: "))
# if 1 % num == num and num % num == 1:
#     print("число")

# 4
# n = int(input("Введите число: "))
# sum_ = 0
# while n > 0:
#     ost = n % 10
#     sum_ = sum_ + ost
#     n = n // 10
# print (sum_)


# 5
n1 = int(input("Введите целое число: "))

# Последнюю цифру первого числа переносим во второе
digit = n1 % 10
n2 = digit

# Избавляемся от последней цифры первого числа
n1 = n1 // 10

while n1 > 0:
    # находим остаток - последнюю цифру
    digit = n1 % 10
    # делим нацело - удаляем последнюю цифру
    n1 = n1 // 10
    # увеличиваем разрядность второго числа
    n2 = n2 * 10
    # добавляем очередную цифру
    n2 = n2 + digit

print('"Обратное" ему число:', n2)




