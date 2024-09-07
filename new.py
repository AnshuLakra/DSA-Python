def mergeSort(customList):
    if len(customList) > 1:
        med = len(customList)//2
        left_list = customList[:med]
        right_list = customList[med:]
        mergeSort(left_list)
        mergeSort(right_list)

        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                customList[k] = left_list[i]
                i += 1
                k += 1
            else:
                customList[k] = right_list[j]
                j += 1
                k += 1
        while i < len(left_list):
            customList[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            customList[k] = right_list[j]
            j += 1
            k += 1
        
    return customList

customList = [3, 2, 5, 4, 1]
print(mergeSort(customList))
