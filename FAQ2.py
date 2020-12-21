n = 10
A = [i for i in range(n+1)]
A.append(4)
A.sort()
G = 0
for i in A:
    if A[i] == A[i+1]:
        G = A[i]
print(G)
