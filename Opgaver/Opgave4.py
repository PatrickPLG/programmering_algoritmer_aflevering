def selection_sort():
    tallist = [2,4,5,1,3,6,9,8,7]
    n = len(tallist)

    for i in range(n-1):
        mini = i
        
        for j in range(i+1,n):
            if tallist[j] < tallist[mini]:
                mini = j
        if mini != i:
            tallist[mini],tallist[i] = tallist[i], tallist[mini]
    return tallist

print(selection_sort())
