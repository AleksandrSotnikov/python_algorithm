def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        res = arr[mid]
        if target == res:
            return mid
        if target < res:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_count_operation(arr, target):
    low = 0
    high = len(arr) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        res = arr[mid]
        if target == res:
            return count
        if target < res:
            high = mid - 1
        else:
            low = mid + 1
    return count
