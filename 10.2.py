def oj():
    L=[-8, 8, 6.0, 5, 'строка', -3.1]
    total=0
    for i in L:
        if type(i)==int or type(i)== float:
            total += i
    print (total)
oj()