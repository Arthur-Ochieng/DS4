def is_sorted(list):
    n = len(list)
    i = 0
    j = 1
    if n == 0 or n == 1:
        return True
    else:
        return list[i] < list[j] and is_sorted(list[j:])

alist = [1,4,10,6,7]
alist2 = [3,4,5,6,7]
print(is_sorted(alist))
print(is_sorted(alist2))