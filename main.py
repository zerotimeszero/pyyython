
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
# a = 0
# for delitel in range(1, num+1):
#     if num % delitel == 0:
#         a+=1
# if a == 2:
#     print("Число простое")
# else:
#     print("Число непростое, такое же как это задание")




# 4
# n = int(input("Введите число: "))
# sum_ = 0
# while n > 0:
#     ost = n % 10
#     sum_ = sum_ + ost
#     n = n // 10
# print (sum_)

# stroka = input("Введите число: ")
# sum_ = 0
# for i in range(len(stroka)):
#     a = int(stroka[i])
#     sum_ += a
# print(sum_)


# 5
# stroka = (input("число: "))
# a = ""
# n = len(stroka) #длина строки
# for i in range(n-1, -1, -1):
#     a += stroka[i]
# print(a)




