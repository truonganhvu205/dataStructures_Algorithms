def mergeTwoSort(lst1, lst2, lst):
    i = j = k = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            lst[k] = lst1[i]
            i += 1
        else:
            lst[k] = lst2[j]
            j += 1

        k += 1

    while i < len(lst1):
        lst[k] = lst1[i]
        i += 1
        k += 1

    while j < len(lst2):
        lst[k] = lst2[j]
        j += 1
        k += 1

def mergeSort(lst):
    if len(lst) <= 1:
        return
    
    mid = len(lst) // 2
    start = lst[mid:]
    end = lst[:mid]

    mergeSort(start)
    mergeSort(end)
    mergeTwoSort(start, end, lst)

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 8, 6, 2, 4]
    mergeSort(lst)

    print(lst)
    