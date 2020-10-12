from random import*
x1 = randint(0,6)
x2 = randint(0,6)
if x1 > x2 :
    print ('Победа первого игрока ')
elif x1 < x2:
    print ('Победил второй игрок ')
else:
    print ('Ничья ')
