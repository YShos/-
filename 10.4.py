from random import randint
def igra():
    N=randint(1,10)
    K=int(input("Угадайте целое число от 1 до 10:"))
    if K==N:
        print("Вы угадали с первой попытки")
    while K!=N:
        K=int(input("Повторите попытку:"))
        if K<N:
            print("Ваше число меньше, чем задумал компьютер")
        elif K>N:
            print("Ваше число больше, чем задумал компьютер")
        else:
            print("Вы угадали")
    print(K)
igra()