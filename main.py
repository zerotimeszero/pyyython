name=input("Введите ваше имя: ")
if name == "Денис":
    print("Денисам запрещенно пользоваться приложением)")
else:
    r = int(input("Какую операцию вы хотите выполнить? "))
    c,d = map(str,input("Введите два числа: ").split())

    if type(c) != int and type(d) != int:
        if r == 1:
            print("Результат:", c + d)
        elif r == 2:
            print("Результат:", c - d)
        elif r == 3:
            print("Результат:", c * d)
        elif r == 4:
            print("Результат:", c / d)
        elif r == 5:
            print("Результат:", c ** d)
        else:
            print("Такой операции нет, до свидания!")
    else:
        print("error")