def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - Left and Right
    Take overall of O(k logn) time 
    """
    mid = (len(list))//2
    left = list[:mid]
    right = list[mid:]
    return left, right  

# def spl1t(list):
#     first = 0
#     last = len(list) - 1
#     midpoint = (first + last)//2

#     while first <= last:


def merge(left, right):
    """
    Merges two lists, and sorts them in the process
    Returns a new merged list
    Takes an overall time of O(n)
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    """
    The two other while loops cater for a situation where the initial list had an odd number of elements init
    """

    while i < len(left):  
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l


def mergesort(list):
    """
    Sorts a list in ascending order
    Creates and returns a new sorted list
    Divide: Find the midpoint of the list and create sublists
    Conquer: Recuisively sorts the sublists created in previous step
    Combine: Merge the sorted sublists created in the previous step
    Takes an overall time of O(nlogn)
    """
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = mergesort(left_half)
    right = mergesort(right_half)

    # print("this is before" ,merge(left,right))
    return merge(left, right)


alist = [54, 56, 67, 12, 76, 45, 23, 15]
v = mergesort(alist)
print(v)

def verify(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify(list[1:])

print(verify(alist))
print(verify(v))



