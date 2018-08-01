"""Selection sort Algo."""

def selection_sort(A):
    length = len(A)
    for index in range(0, length):
        min = index
        for j in range(index+1, length):
            if A[j] < A[min]:
                min = j
        temp = A[min]
        A[min] = A[index]
        A[index] = temp
    print(A)


selection_sort([5, 3, 8, 1, 2])
