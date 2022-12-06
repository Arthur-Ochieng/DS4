from linked_list import Linked_list

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    Recursively divides the linked list into sublists containng a single node
    Repeatedly merge the sublists to produce sorted sublists until one remains
    Runs in 0(k nlog n) time
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head == None:
        return linked_list

    left_half, right_half =  split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted linked list at midpoint into sublsits
    Takes 0(K log n)
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = Linked_list()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half 


def merge(left, right):
    """
    Merges two linked list sorting by data in the nodes
    Returns a new merged list
    Runs in 0(n) time
    """
    # Create a new linked list that contains nodes from merging left and right
    merged = Linked_list()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # If the head node of left is null, we are past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to false
            right_head = right_head.next_node
        
        # If the head of right is none, were past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set the loop condition to false
            left_head = left_head.next_node
        else:
            # Not at either tail node 
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on the left is less than that on the right, move current to the next node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # If data on the left is greater than that on the right, move current to the next node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node
    
    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

l = Linked_list()
l.add(10)
l.add(24)
l.add(12)
l.add(65)
l.add(75)

print(l)
sorted_linked_list =  merge_sort(l)
print(sorted_linked_list)