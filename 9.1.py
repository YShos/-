L = [3, 6, 7, 4, -5, 4, 3, -1]

if sum(L) > 2 :
    print ('число элементов списка: ',len(L))

raznost = max(L) - min(L)
if raznost > 10 :
    print (sorted(L))
else:
    print ('Разность меньше 10')
