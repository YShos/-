import doctest

def w_d (x):
    q = x**4 + 4**x
    return q
  

x = int(input('Введите число: '))
print (doctest.testmod(w_d(x)))

