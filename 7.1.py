from math import*
def Q(p):
    p = (a + b + c) / 2
    s = float(sqrt(p*(p - a)*(p - b)*(p - c)))
    return s

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))
p = (a + b + c) / 2
print('Площадь треугольника равна: ', round(Q(p), 2))
