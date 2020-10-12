s = "У лукоморья 123 дуб зеленый 456"

if s.count('я') == 1 :
    print ('Индекс буквы я: ', s.find('я'))
else:
    print ('буквы Я в тесте  нету ')
    
d = s.lower() 
print ('Количество букв у: ', d.count ('у'))

if s.isalpha() == True :
    print ('Строка состоит только из букв')
else:
    print (s.upper())

if len(s) > 4:
    print (s.lower())

b = s.replace(s[0], 'О')
print(b)

