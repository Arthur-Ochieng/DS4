import random

def is_sorted(list):
    for index in range(len(list)-1):
        if list[index] > list[index + 1]:
            return False
    return True

def bogo_sort(list):
    count = 0
    while not is_sorted(list):
        random.shuffle(list)
        count += 1
    return list,count

alist = [1,4,10,6,7]
alist2 = [3,4,5,6,7]
print(bogo_sort(alist))
print(bogo_sort(alist2))