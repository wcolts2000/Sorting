# TO-DO: Complete the selection_sort() function below
'''
Find the smallest card. Swap it with the first card.
Find the second-smallest card. Swap it with the second card.
Find the third-smallest card. Swap it with the third card.
Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.
'''


def selection_sort(arr):
    # loop through n-1 elements

    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        if smallest_index != i:
            swap(arr, i, smallest_index)
        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
'''
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
'''


def bubble_sort(arr):
    # for i in range(0, len(arr) - 1):
    #     for j in range(0, len(arr) - 1 - i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    swapped = False
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
