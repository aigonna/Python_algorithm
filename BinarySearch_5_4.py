def BinarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

# testlist = [0, 1, 2, 8, 13, 17, 29, 67]
# print(BinarySearch(testlist, 3))
# print(BinarySearch(testlist, 13))

def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)
testlist = [0, 1, 2, 8, 13, 17, 19, 33, 78]
print(binarySearch(testlist, 8))
print(binarySearch(testlist, 13))
