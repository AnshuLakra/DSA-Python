# Bubble Sort


# def bubbleSort(customList):
#     for i in range(len(customList)-1):
#         for j in range(len(customList)-i-1):
#             if customList[j] > customList[j + 1]:
#                 customList[j] , customList[j+1] = customList[j+1] ,customList[j]
#                 # temp = customList[j]
#                 # customList[j] = customList[j+1]
#                 # customList[j+1] = temp

#     print(customList)


# customList = [2, 1, 5, 3, 9, 7, 4, 6, 8]
# bubbleSort(customList)


# Selection Sort

# def selectionSort(customList):
#     for i in range(len(customList)):
#         min_index = i
#         for j in range(i+1, len(customList)):
#             if customList[min_index] > customList[j]:
#                 min_index = j
#         customList[i], customList[min_index] = customList[min_index], customList[i]
#     print(customList)


# customList = [2, 1, 5, 3, 9, 7, 4, 6, 8]
# selectionSort(customList)

# InsertionSort

# import math


# def insertionSort(customList):
#     for i in range(1, len(customList)):
#         key = customList[i]
#         j = i - 1
#         while j >= 0 and key < customList[j]:
#             customList[j + 1] = customList[j]
#             j -= 1
#         customList[j + 1] = key
#     # print(customList)
#     return customList


# customList = [2, 1, 5, 3, 9, 7, 4, 6, 8]
# insertionSort(customList)
# print(insertionSort(customList))


# BucketSort


# def bucketSort(customList):
#     numberOfBucket = round(math.sqrt(len(customList)))
#     maxElement = max(customList)
#     arr = [[] for _ in range(numberOfBucket)]

#     for i in customList:
#         index_b = math.ceil(i*numberOfBucket/maxElement)
#         arr[index_b - 1].append(i)
#     # print(arr)
#     # for i in range(numberOfBucket):
#     #     arr[i] = insertionSort(arr[i])
#         # test.append(insertionSort(arr[i]))
#     # k = 0
#     # for i in range(numberOfBucket):
#     #     for j in range(numberOfBucket):
#     #         customList[k] = arr[i][j]
#     #         k += 1
#     # print(arr)
#     # print(customList)

#     sorted_arr = []
#     for i in range(numberOfBucket):
#         arr[i] = insertionSort(arr[i])
#         sorted_arr.extend(arr[i])

#     print(sorted_arr)


# customList = [2, 1, 5, 3, 9, 7, 4, 6, 8]
# bucketSort(customList)


# MergeSort

# def mergeSort(customList):
#     if len(customList) > 1:
#         mid = len(customList)//2
#         left_list = customList[:mid]
#         right_list = customList[mid:]
#         mergeSort(left_list)
#         mergeSort(right_list)

#         i = 0
#         j = 0
#         k = 0
#         while i < len(left_list) and j < len(right_list):
#             if left_list[i] < right_list[j]:
#                 customList[k] = left_list[i]
#                 i += 1
#                 k += 1
#             else:
#                 customList[k] = right_list[j]
#                 j += 1
#                 k += 1
#         while i < len(left_list):
#             customList[k] = left_list[i]
#             i += 1
#             k += 1
#         while j < len(right_list):
#             customList[k] = right_list[j]
#             j += 1
#             k += 1
#     return customList


# customList = [2, 1, 5, 3, 9, 7, 4, 6, 8]
# print(mergeSort(customList))


# QuickSort


def swap(customList, index_1, index_2):
    # temp= customList[index_1]
    # customList[index_1] = customList[index_2]
    # customList[index_2] =
    customList[index_1], customList[index_2] = customList[index_2], customList[index_1]


def pivot(customList, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if customList[i] < customList[pivot_index]:
            swap_index += 1
            swap(customList, swap_index, i)
    swap(customList, pivot_index, swap_index)

    # print(customList)
    return swap_index


def quickSort(customList, left, right):
    if left < right:
        pivot_index = pivot(customList, left, right)
        quickSort(customList, left, pivot_index - 1)
        quickSort(customList, pivot_index + 1, right)
    return customList


customList = [3, 5, 0, 6, 2, 1, 4]
# print(pivot(customList, 0, 6))
# print(customList)


print(quickSort(customList, 0, 6))
