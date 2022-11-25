def binary_search(list, target):
    first = 0
    last = len(list) - 1        # You want the value to point to the index of the element in the array
# Both of the above operations run in constant time

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif [midpoint] < target: 
            first = midpoint + 1          
        else: 
            last = midpoint - 1
# The comparison operations all run at constant time
# The while loop cause the logarithmic time since the last and first are changed until it satisfies
    return None;


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers, 6)

verify(result)

# The code runs only when the list is sorted, if not the code might return none even if the number already exists in the list