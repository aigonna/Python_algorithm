def bubbleSort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp

# alist = [1, 23, 3, 45, 27, 78, 49]
# bubbleSort(alist)
# print(alist)

def shortBubbleSort(alist):
    exchangs = True
    exchangeNums = len(alist) - 1
    while exchangeNums > 0 and exchangeNums:
        exchangs = False
        for i in range(exchangeNums):
            if alist[i] > alist[i+1]:
                exchangs = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

        exchangeNums -= 1
    return alist

alist = [1, 23, 3, 45, 27, 78, 49]
print(shortBubbleSort(alist))


