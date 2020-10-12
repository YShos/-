def Ferengate(TC):
    TF =  9/5 * TC + 32
    return TF

TC = int(input('Введите градусы по шкале Цельсия: '))
a = Ferengate(TC)
print ('Температура в градусах по шкале Фаренгейта:', a)
