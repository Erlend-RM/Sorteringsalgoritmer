def sort(A):
    n = len(A)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j + 1]:
                A[j],A[j + 1] = A[j + 1], A[j]

    return A

