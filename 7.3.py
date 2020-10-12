from math import*

def primer(x):
    v = sqrt (1 - sin(x))
    return v

x = float(int(input('Введите значение х: ')))
print ('Ответ: ', primer(x))
