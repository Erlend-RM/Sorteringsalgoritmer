def buildMaxHeap(A, n):
    for i in range(n//2, -1, -1):
        bubbledown(A, i, n)

def bubbledown(A, i, n):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and A[largest] < A[left]:
        largest, left = left, largest

    if right < n and A[largest] < A[right]:
        largest, right = right, largest

    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        bubbledown(A, largest, n)

def sort(A):
    n = len(A)
    buildMaxHeap(A, n)

    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        bubbledown(A, 0, i)
    return A


