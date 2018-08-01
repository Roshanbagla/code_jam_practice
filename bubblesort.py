"""Bubble Sort."""


def bubblesort(A):
    length = len(A)
    print(length)
    for index in range(0, length):
        for j in range(0, length-index-1):
            print ("The value of J", j)
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

    print(A)


bubblesort([2, 7, 4, 1, 5, 3])
