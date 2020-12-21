a = list(map(int,input().split()))
c=[]
if len(a) != len(set(a)):
    c = [i for i in a if a.count(i) >= 2]
print(c)
