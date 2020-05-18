# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc)
    # Your code here

    # TO-DO: swap
    # Your code here

    # set first number as the minimum, then compare to every number towards the right
    # when a higher number is found, that become the new minimum and process repeats
    # minimum value gets moved to the left
    # left side becomes sorted, right becomes unsorted

    # use -1 so at the lasy iteration, the last number remaining becomes the newest minimum value
    indexing_length = range(0, len(arr) - 1)

    for i in indexing_length:
        # set i to min value so the first item in the sorted list becomes the min value every iteration
        min_value = i
        # i + 1 for all elements to the right of the min value
        for j in range(i + 1, len(arr)):
            # replace min value if element to the right is greater than min value
            if arr[j] < arr[min_value]:
                min_value = j
        # if we find a lower than min, switch those values
        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]
    # return array
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    indexing_length = len(arr) - 1
    # use this variable to break out of the array when the list has been sorted
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            # if item to the left is greater than the right, say sorted is false and flip the two items
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    # when the list gets sorted, the while loop will not trigger, keeping sorted to True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr
