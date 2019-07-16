# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # TO-DO
    merged_arr = []
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        if arrB[j] > arrA[i]:
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1
    while i < len(arrA):
        merged_arr.append(arrA[i])
        i+=1
    while j < len(arrB):
        merged_arr.append(arrB[j])
        j+=1
    return merged_arr

arr1 = [1,3,5,7]
arr2 = [2,6,9,10]
arr3 = merge(arr1, arr2)
print(arr3)
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
        # TO-DO
    # midpoint = len(arr) // 2
    # left = []
    # right = []
    # if len(arr) > 1:
    #     left = arr[:midpoint]
    #     right = arr[midpoint:]
    #     merge_sort(left)
    #     merge_sort(right)

    # merge(left, right)

    return arr


arr = [1, 9, 5, 3]
# merge_sort(arr)
# print(arr)
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
