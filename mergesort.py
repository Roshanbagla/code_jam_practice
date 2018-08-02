"""Merge Sort, Uses the concept of divide and conquer."""


def merge(left, right, Array):
    i = 0
    j = 0
    k = 0

    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            Array[k] = left[i]
            i = i+1
        else:
            Array[k] = right[j]
            j = j+1
        k = k+1

    while (i < len(left)):          # left over elements (only one of 2 while
        Array[k] = left[i]           # loops will be executed)
        i += 1
        k += 1

    while (j < len(right)):
        Array[k] = right[j]
        j += 1
        k += 1


def mergesort(Array):
    """Function for dividing and calling merge sort."""
    n = len(Array)
    if n < 2:
        return
    mid = n//2
    left = []
    right = []
    left = Array[:mid]
    right = Array[mid:]

    mergesort(left)
    mergesort(right)
    merge(left, right, Array)


Array = [99, 21, 19, 22, 28, 11, 14]
mergesort(Array)
print (Array)
