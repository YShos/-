def Quatro (a,b,c):
    Quat = (a+b+c)/3
    return Quat


a,b,c = map(int,input('Введите три числа:').split())
print (Quatro (a,b,c))
