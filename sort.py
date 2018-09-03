import random
def sift(data, low, high):
    i = low
    j = 2*i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] < data[j + 1]:
            j += 1
        if tmp < data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp

def heap_sort(data):
    first = len(data) // 2 - 1
    for i in range(first, -1, -1):
        sift(data, i, len(data)-1)
    print(data)

data = list(range(10000))
random.shuffle(data)
heap_sort(data)