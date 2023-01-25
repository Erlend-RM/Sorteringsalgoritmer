def sort(A):
    n = len(A)
    for i in range(n):
        j = i
        while j > 0 and A[j-1] > A[j]:
            #A[j-1], A[j] = A[j], A[j-1]
            A.swap(j, j-1)
            j = j - 1
        
    return A

