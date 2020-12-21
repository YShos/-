n = 100
A = [i for i in range(n+1)]
sum = 0
del A[19]
for i in A:
    sum += i
M = n * (n+1)//2

D = M - sum
print(D)