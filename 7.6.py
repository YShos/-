from math import*
x,y = map(int,input('Введите два числа: ').split())
z = ( x + ((2+y) / x**2 ) / (y+(1 / sqrt(x**2 + 10))))
q = 2.8 * sin(x) + abs(y)
print (round(z,2),round(q,3))
