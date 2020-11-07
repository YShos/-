def cddd():
    a = [4, 6, 7, 8, 1, 5]
    b = len(a) // 2
    for i in range(b):
        temp = a[b]
        a[b] = a[i]
        a[i] = temp
        b = b + 1
    print(a)
cddd()