def finder_smallest_number_index(arr):
    if len(arr) == 0:
        return None
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def finder_largest_number_index(arr):
    if len(arr) == 0:
        return None
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index


def finder_smallest_number(arr):
    if len(arr) == 0:
        return None
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest


def finder_largest_number(arr):
    if len(arr) == 0:
        return None
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


def selection_sort_ascending(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = finder_smallest_number_index(arr)
        if smallest is not None:
            sorted_arr.append(arr.pop(smallest))
    return sorted_arr


def selection_sort_descending(arr):
    sorted_arr = []
    for i in range(len(arr)):
        largest = finder_largest_number_index(arr)
        if largest is not None:
            sorted_arr.append(arr.pop(largest))
    return sorted_arr
