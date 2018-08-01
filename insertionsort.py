"""Insertion Sort."""

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        index = j-1
        while (index >= 0 and A[index] > key):
            A[index+1] = A[index]
            index = index - 1
        A[index+1] = key
    print(A)


insertion_sort([6, 9, 5, 0, 8, 2, 7, 1, 3])
insertion_sort([4, 0, 1, 2, 6, 9, 12, 23, 34])
