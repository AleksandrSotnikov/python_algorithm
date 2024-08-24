"""
Этот модуль реализует алгоритмы бинарного поиска.
"""


def binary_search(arr, target):
    """
    Выполняет бинарный поиск в отсортированном массиве для нахождения индекса целевого значения.

    Параметры:
    arr (list): Список отсортированных элементов.
    target: Элемент, который нужно найти в списке.

    Возвращает:
    int: Индекс целевого элемента, если он найден, иначе None.
    """
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
    """
    Выполняет бинарный поиск в отсортированном массиве и подсчитывает количество операций,
    необходимых для нахождения целевого значения.

    Параметры:
    arr (list): Список отсортированных элементов.
    target: Элемент, который нужно найти в списке.

    Возвращает:
    int: Количество выполненных операций во время поиска.
         Возвращает количество, даже если целевой элемент не найден.
    """
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
