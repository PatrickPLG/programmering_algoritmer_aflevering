#https://en.wikipedia.org/wiki/Selection_sort

talliste = [0,2,5,4,3,6,9,7,8]
i = 0

def selectionSort(A):
    maxValue = len(A)-1
    nextValue = max(A)

    for i in range(i = maxValue - 1): #Ved ikke
        if A[i] > nextValue:
            nextValue = A[i]
    while (maxValue > 0) and (A[maxValue] = nextValue):
        maxValue = maxValue - 1
    
    while maxValue > 0:
        value = nextValue
        nextValue = A[maxValue]
        for #Ved ikke:
            if A[i] = value:
                