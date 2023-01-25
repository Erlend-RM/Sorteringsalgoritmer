def sort(A):
    n = len(A)
    for i in range(n):
        k = i
        
        for j in range(i+1,n):
            if A[j] < A[k]:
                k = j
        
        if i != k:
            #A[i], A[k] = A[k], A[i]
            A.swap(i, k)
    return(A)
