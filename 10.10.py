from random import randint
def matriza():
    N = int(input("Количество столбцов: "))
    M = int(input("Количество строк: "))
    lst=[[randint(1, 9) for i in range(N)] for i in range(M)]
    for i in lst:
        print()
        for j in i:
            print (j, end=" ")
matriza()