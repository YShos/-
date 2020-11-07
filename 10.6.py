def schet():
    total = 0
    while True:
        n = input("Введите число или стоп для вывода: ")
        if n == "стоп":
            print("До встречи!")
            break
        else:
            total = total + int(n)
            print("сумма равна:", total)
schet()
