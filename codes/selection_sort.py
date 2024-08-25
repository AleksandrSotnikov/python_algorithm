"""
Модуль для выполнения поиска индексов и значений наименьших и наибольших элементов в массиве,
а также для сортировки массива методом выбора.
"""


def finder_smallest_number_index(arr):
    """
    Возвращает индекс наименьшего элемента в массиве.

    :param arr: Список чисел.
    :return: Индекс наименьшего элемента или None, если массив пуст.
    """
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
    """
    Возвращает индекс наибольшего элемента в массиве.

    :param arr: Список чисел.
    :return: Индекс наибольшего элемента или None, если массив пуст.
    """
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
    """
    Возвращает наименьший элемент в массиве.

    :param arr: Список чисел.
    :return: Наименьший элемент или None, если массив пуст.
    """
    if len(arr) == 0:
        return None
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest


def finder_largest_number(arr):
    """
    Возвращает наибольший элемент в массиве.

    :param arr: Список чисел.
    :return: Наибольший элемент или None, если массив пуст.
    """
    if len(arr) == 0:
        return None
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


def selection_sort_ascending(arr):
    """
    Сортирует массив по возрастанию с использованием метода выбора.

    :param arr: Список чисел.
    :return: Новый отсортированный список.
    """
    sorted_arr = []
    while arr:
        smallest = finder_smallest_number_index(arr)
        if smallest is not None:
            sorted_arr.append(arr.pop(smallest))
    return sorted_arr


def selection_sort_descending(arr):
    """
    Сортирует массив по убыванию с использованием метода выбора.

    :param arr: Список чисел.
    :return: Новый отсортированный список.
    """
    sorted_arr = []
    while arr:
        largest = finder_largest_number_index(arr)
        if largest is not None:
            sorted_arr.append(arr.pop(largest))
    return sorted_arr
