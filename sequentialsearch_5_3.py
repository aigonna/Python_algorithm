def sequential(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

#testlist = [1, 2, 32, 8, 17]
#print(sequential(testlist, 3))
#print(sequential(testlist, 17))

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found

testlist = [0, 12, 22, 145, 223, 554]
print(orderedSequentialSearch(testlist, 223))
print(orderedSequentialSearch(testlist, 1)) #O(n)


