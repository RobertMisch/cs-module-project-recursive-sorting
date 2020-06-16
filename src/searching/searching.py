import math
# TO-DO: Implement a recursive implementation of binary search
#remember to add the return so the recursive functions bubble up
def binary_search(arr, target, start, end):
    # Your code here
    left_bound=start
    right_bound=end
    position= math.floor(left_bound+right_bound/2)
    if left_bound>right_bound:
            return -1
    elif target < arr[position]:
        return binary_search(arr, target, left_bound, position-1)
        #iterative version
        # right_bound=position-1
        # position= math.floor(left_bound+right_bound/2)
    elif target > arr[position]:
        return binary_search(arr, target, position+1, right_bound)
        # left_bound=position+1
        # position= math.floor(left_bound+right_bound/2)
    elif target == arr[position]:
        return position


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

