def sort(A):
    low = 0
    high = len(A) - 1
    
    def partition(A, low, high):
        #p = (low + high) //2
        pivot = A[high]
        left = low
        right = high - 1
        while left <= right:
            while left <= right and A[left] <= pivot:
                left = left + 1
            while right >= left and A[right] >= pivot:
                right = right - 1
            if left < right:
                #A[left],A[right] = A[right],A[left]
                A.swap(left, right)
        #A[left],A[high] = A[high],A[left]
        A.swap(left, high)
        return left

    def quicksort(A, low, high):
        if low >= high:
            return A
        p = partition(A, low, high)
        quicksort(A, low, p - 1)
        quicksort(A, p + 1, high)
        return A
    quicksort(A, low, high)
    return A

    


