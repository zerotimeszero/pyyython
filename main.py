# 1
# def polymorph(p):
#     p = p[::-1]
#
#     return p
#
# u_n = input()
#
# if u_n == polymorph(u_n):
#     print("Число является полиморфом")
# else:
#     print("Не является полихромом")



# 2
# def vowel_count(x):
#     count = 0
#     x = x.lower()
#     for i in range(len(x)):
#         # if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
#         if x[i] in "aeiou":
#             count += 1
#     return count
#
# string = input("Строка: ")
# print(vowel_count(string))
# test1 = "aaabbb"
# if (vowel_count(test1) == 3): print("TEST PASSED")
# else: print("TEST FAILED")




# alternative
# string = input("Строка: ").lower()
# count = 0
# for i in range(len(string)):
#     # if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
#     if string[i] in "aeiou":
#         count += 1
# print(count)




# 3
# def count_slovo(s):
#     count = 1
#     for i in range(len(s)):
#         if s[i] == " ":
#             count += 1
#     return count
#
#
# word_test = input("слова: ")
# print(count_slovo(word_test))



#
# word_test = input("слова: ")
# count = 1
# for i in range(len(word_test)):
#     if word_test[i] == " ":
#         count += 1
# print(count)


# alternative
# def smart_len(stroka):
#     return len(stroka.split())
#
#
# test = "word word word word word                    "
#
# print(smart_len(test))



# alternative

# def evrica(dick):
#     dick = dick.split()
#     return len(dick)
#
# word_test = input("слово: ")
# print(evrica(word_test))



# word_test = input("слово: ").split()
# print(len(word_test))


# 4

# a = int(input())              16
# b = int(input())              13
#
# while a != 0 and b != 0:      пока a не равно 0 и b не равно 0, выполнять:
#     if a > b:                     если a больше b:
#         a = a % b                     а становится остатком от деления а на b
#     else:                         иначе:
#         b = b % a                     b становится остатком от деления b на a
#                               выведи а+b
#                                       a = 3
#                                       b = 1


# def NOD(x, c):
#
#     while x != 0 and c != 0:
#         if x > c:
#             x = x % c
#         else:
#             c = c % x
#
#     return x + c
#
#
# a = int(input())
# b = int(input())
#
# print(NOD(a, b))



# a = int(input())
# b = int(input())
#
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
#
# print(a + b)
