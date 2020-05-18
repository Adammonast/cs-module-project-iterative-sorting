# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # TO-DO: swap
        # Your code here

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
