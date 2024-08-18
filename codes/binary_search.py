def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)
        res = arr[mid]
        if target == res:
            return mid
        if target < res:
            high = mid-1
        else:
            low = mid+1
    return None


