def schet():
    n = input("Введите число: ")
    sm = 0
    n = list(map(int, n))
    for i in n:
        if i % 2 != 0:
            sm += i**2
    print("Сумма квадратов нечетных чисел равна:", sm)
schet()