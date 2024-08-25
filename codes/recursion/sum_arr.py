"""
Модуль содержит функции для суммирования элементов массива.
"""


def sum_arr(arr):
    """
    Возвращает сумму всех элементов массива.

    :param arr: Список чисел
    :return: Сумма элементов списка
    """
    summa = 0
    while arr:
        summa += arr.pop(0)
    return summa


def sum_arr_recursive(arr):
    """
    Рекурсивно возвращает сумму всех элементов массива.

    :param arr: Список чисел
    :return: Сумма элементов списка
    """
    if len(arr) == 0:
        return 0
    return arr[0] + sum_arr_recursive(arr[1:])
