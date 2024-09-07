# Linear Search


# def linearSearch(sampleList,value):
#     for i in sampleList:
#         if i == value:
#             return True
#     return False


# sampleList = [1,4,2,6,7,5]
# print(linearSearch(sampleList,60))


# Binary Search


import math


def binarySearch(sampleList, value):
    start = 0
    end = len(sampleList) - 1
    middle = math.floor((start+end)/2)
    while not (sampleList[middle] == value) and start <= end:
        if value > middle:
            start = middle + 1
        else:
            end = middle - 1
        middle = math.floor((start+end)/2)
        print(start, middle, end)

    if sampleList[middle] == value:
        return True
    else:
        return False


sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(binarySearch(sampleList, 80))
