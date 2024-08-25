"""
Модуль с реализацией алгоритма быстрой сортировки.
"""


def quik_sort(arr):
    """
    Выполняет быструю сортировку массива.

    :param arr: Массив чисел для сортировки
    :return: Отсортированный массив
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quik_sort(less) + [pivot] + quik_sort(greater)
