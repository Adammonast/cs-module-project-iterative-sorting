def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    begin_index = 0  # left
    end_index = len(arr) - 1  # right

    while begin_index <= end_index:
        midpoint = (begin_index + end_index) // 2

        if arr[midpoint] == target:
            return midpoint
        if arr[midpoint] < target:
            begin_index = midpoint + 1
        else:
            end_index = midpoint - 1

    return -1  # not found
