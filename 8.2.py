def text(s,n):
    if len(s) > n:
        print(s.upper())
    else:
        print(s)
s = input('Введите текст: ')
n = int(input('Введите число: '))
print (text(s,n))
