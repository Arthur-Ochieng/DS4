def quicksort(list):
    if len(list) <= 1:
        return list
    less_than_pivot = []
    great_than_pivot = []
    pivot = list[0]
    # print(list)
    for i in list[1:]:
        if i < pivot:
            less_than_pivot.append(i)
        else:
            great_than_pivot.append(i)
    print("%15s %1s %-15s" % (less_than_pivot, pivot, great_than_pivot))    
    return quicksort(less_than_pivot) + [pivot] + quicksort(great_than_pivot)

alist = [11,2,44,15,6,9,7]
verify = quicksort(alist)
print(verify)