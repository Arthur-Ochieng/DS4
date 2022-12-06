# Trying out linear search on a list

def linear(list, target):
    position = 0
    current = len(list)
    while position < current:
        if list[position] == target:
            return True
        else:
            position += 1
        
    return False

def verify(result):
    print(result)

alist = [1, 2, 3, 4, 5]
target = 4
result = linear(alist, target)
verify(result)

alist = [1, 2, 3, 4, 5]
target = 12
result = linear(alist, target)
verify(result)
