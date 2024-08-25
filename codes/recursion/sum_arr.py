def sum_arr(arr):
    summa = 0
    while arr:
        summa += arr.pop(0)
    return summa


def sum_arr_recursive(arr):
    if len(arr) == 0:
        return 0
    arr[0] += sum_arr_recursive(arr[1:])
    return arr[0]
