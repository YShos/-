from random import*

l =  ['самовар', 'весна', 'лето']
b = choice(l) #случайное слово
c = choice(b) # случайная буква
d = list(b) #список букв из слова
e = b.index(c)
d[e] = '?'
f = ''.join(d)     
print(f)

j = input('Введите букву: ')
if j == c:
    print('Победа!')
else:
    print('Попробуйте еще раз :( ')
