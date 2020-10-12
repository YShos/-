from math import*
x = float(input('Введите число: '))
if x >= 0.2 and x <= 0.9 :
    f = sin(x)
else:
    f = 1
print (round(f,3))
