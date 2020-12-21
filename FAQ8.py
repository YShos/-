def f(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

l = list(map(int,input().split()))
print (f(l))
