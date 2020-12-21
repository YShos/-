def f(l):
    n = []
    for i in l:
        if not n or i != n[-1]:
            n.append(i)
    return n
l = list(map(int,input().split()))
print (f(l))
