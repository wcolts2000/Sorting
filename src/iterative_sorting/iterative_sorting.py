# TO-DO: Complete the selection_sort() function below
'''
Find the smallest card. Swap it with the first card.
Find the second-smallest card. Swap it with the second card.
Find the third-smallest card. Swap it with the third card.
Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.
'''


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(arr):
    # loop through n-1 elements

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


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# selection_sort(arr1)
# print(arr1)

# TO-DO:  implement the Bubble Sort function below
'''
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
'''


def bubble_sort(arr):

    # for i in range(len(arr), 0, -1):
    #     for j in range(len(arr)-1):
    #         if arr[j] < arr[j+1]:
    #             swap(arr, arr[j], arr[j+1])
    #     # if arr[j]
    # return arr
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                swap(arr, arr[j], arr[j+1])
    return arr


bubble_sort(arr1)
print(arr1)
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
