def bucketsort(A):
    B = []
    n = len(A)
    N = len(B)

    for i in range(n):
        B.append([])

    for i in range(n):
        k = A[i]
        B[i].append(k)

    j = 0
    for k in range(N):
        for x in B[k]:
            A[j] = x
            j += 1
    return A


A = [12,345,6,2,0,435,63,43,26,28,385,56]
print(bucketsort(A))