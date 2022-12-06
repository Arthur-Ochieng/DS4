def selection_sort(list):
    sorted_list = []
    print("%-25s %-25s" % (list, sorted_list))
    for i in range(0,len(list)):
        moving_index = index_min(list)
        sorted_list.append(list.pop(moving_index))
        print("%-25s %-25s" % (list, sorted_list))
    return sorted_list 

def index_min(list):
    min_index = 0 
    for i in range(1, len(list)):
        if list[i] < list[min_index]:
            min_index = i
    return min_index

alist = [11,2,44,15,6,9,7]
verify = selection_sort(alist)
print(verify)