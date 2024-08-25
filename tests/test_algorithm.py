"""
Модуль для тестирования алгоритмов поиска и сортировки,
а также работы с фабрикой предметов и рекурсией.
"""

import unittest

from codes.binary_search import binary_search, binary_search_count_operation
from codes.recursion.fact import fact
from codes.recursion.item import ItemFactory, ItemType, Item, Box, Key
from codes.recursion.sum_arr import sum_arr, sum_arr_recursive
from codes.selection_sort import (
    finder_smallest_number_index,
    finder_largest_number_index,
    finder_smallest_number,
    finder_largest_number,
    selection_sort_ascending,
    selection_sort_descending
)


class AlgorithmTestCase(unittest.TestCase):
    """Тесты для алгоритмов поиска и сортировки."""

    def test_binary_search(self):
        """Тест для бинарного поиска."""
        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(binary_search(int_list, 25), None)
        self.assertEqual(binary_search(int_list, 12), 11)

    def test_binary_search_count_operation(self):
        """Тест для подсчета операций в бинарном поиске."""
        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(binary_search_count_operation(int_list, 5), 2)
        self.assertEqual(binary_search_count_operation(int_list, 6), 4)

    def test_finder_smallest_number_index(self):
        """Тест для нахождения индекса наименьшего элемента."""
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(finder_smallest_number_index(int_list), 3)
        self.assertEqual(finder_smallest_number_index(none_list), None)

    def test_finder_largest_number_index(self):
        """Тест для нахождения индекса наибольшего элемента."""
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(finder_largest_number_index(int_list), 0)
        self.assertEqual(finder_largest_number(none_list), None)

    def test_finder_smallest_number(self):
        """Тест для нахождения наименьшего элемента."""
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(finder_smallest_number(int_list), 1)
        self.assertEqual(finder_smallest_number(none_list), None)

    def test_finder_largest_number(self):
        """Тест для нахождения наибольшего элемента."""
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(finder_largest_number(int_list), 6)
        self.assertEqual(finder_largest_number(none_list), None)

    def test_selection_sort_ascending(self):
        """Тест для сортировки массива по возрастанию."""
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(selection_sort_ascending(none_list), [])
        self.assertEqual(selection_sort_ascending(int_list), [1, 2, 3, 4, 5, 6])

    def test_selection_sort_descending(self):
        """Тест для сортировки массива по убыванию."""
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(selection_sort_descending(none_list), [])
        self.assertEqual(selection_sort_descending(int_list), [6, 5, 4, 3, 2, 1])


class TestItem(unittest.TestCase):
    """Тесты для предметов и фабрики предметов."""

    def test_item_creation(self):
        """Тест создания предмета."""
        item = ItemFactory.create_item(ItemType.ITEM)
        self.assertEqual(item.get_item_type(), ItemType.ITEM)
        self.assertIsInstance(item, Item)

    def test_key_creation(self):
        """Тест создания ключа."""
        key = ItemFactory.create_item(ItemType.KEY)
        self.assertEqual(key.get_item_type(), ItemType.KEY)
        self.assertIsInstance(key, Key)

    def test_box_creation_without_items(self):
        """Тест создания коробки без предметов."""
        box = ItemFactory.create_item(ItemType.BOX)
        self.assertEqual(box.get_item_type(), ItemType.BOX)
        self.assertIsInstance(box, Box)
        self.assertEqual(len(box.items), 0)

    def test_box_creation_with_items(self):
        """Тест создания коробки с предметами."""
        key = ItemFactory.create_item(ItemType.KEY)
        item = ItemFactory.create_item(ItemType.ITEM)
        box = ItemFactory.create_item(ItemType.BOX, [key, item])
        self.assertEqual(box.get_item_type(), ItemType.BOX)
        self.assertIsInstance(box, Box)
        self.assertEqual(len(box.items), 2)
        self.assertIsInstance(box.items[0], Key)
        self.assertIsInstance(box.items[1], Item)

    def test_factory_returns_correct_types(self):
        """Тест корректного возвращения типов фабрикой."""
        key = ItemFactory.create_item(ItemType.KEY)
        box = ItemFactory.create_item(ItemType.BOX, [])
        item = ItemFactory.create_item(ItemType.ITEM)

        self.assertIsInstance(key, Key)
        self.assertIsInstance(box, Box)
        self.assertIsInstance(item, Item)

    def test_is_a_box(self):
        """Тест проверки, является ли объект коробкой."""
        box = Item(ItemType.BOX)
        self.assertTrue(box.is_a_box())
        self.assertFalse(box.is_a_key())
        self.assertFalse(box.is_a_item())

    def test_is_a_key(self):
        """Тест проверки, является ли объект ключом."""
        key = Item(ItemType.KEY)
        self.assertTrue(key.is_a_key())
        self.assertFalse(key.is_a_box())
        self.assertFalse(key.is_a_item())

    def test_is_a_item(self):
        """Тест проверки, является ли объект предметом."""
        item = Item(ItemType.ITEM)
        self.assertTrue(item.is_a_item())
        self.assertFalse(item.is_a_box())
        self.assertFalse(item.is_a_key())

    def test_get_items(self):
        """Тест получения предметов из коробки."""
        key = Item(ItemType.KEY)
        item = Item(ItemType.ITEM)
        box = Box([key, item])

        items = box.get_items()
        self.assertEqual(len(items), 2)
        self.assertIs(items[0], key)
        self.assertIs(items[1], item)


class LookForKeyTestCase(unittest.TestCase):
    """Тесты для поиска ключа в коробке."""

    def test_key_in_main_box(self):
        """Тест нахождения ключа в основной коробке."""
        key = Item(ItemType.KEY)
        main_box = Box([key])

        found_key = main_box.look_for_key()
        self.assertIsNotNone(found_key)
        self.assertTrue(found_key.is_a_key())

    def test_key_in_inner_box(self):
        """Тест нахождения ключа во внутренней коробке."""
        key = Item(ItemType.KEY)
        inner_box = Box([key])
        main_box = Box([Item(ItemType.ITEM), inner_box])

        found_key = main_box.look_for_key()
        self.assertIsNotNone(found_key)
        self.assertTrue(found_key.is_a_key())

    def test_key_not_found(self):
        """Тест, когда ключ не найден."""
        main_box = Box([Item(ItemType.ITEM), Box([Item(ItemType.ITEM)])])

        found_key = main_box.look_for_key()
        self.assertIsNone(found_key)

    def test_multiple_boxes_with_key(self):
        """Тест нахождения ключа в нескольких коробках."""
        key = Item(ItemType.KEY)
        inner_box1 = Box([Item(ItemType.ITEM)])
        inner_box2 = Box([key])
        main_box = Box([inner_box1, inner_box2])

        found_key = main_box.look_for_key()
        self.assertIsNotNone(found_key)
        self.assertTrue(found_key.is_a_key())

    def test_empty_box(self):
        """Тест, когда коробка пустая."""
        main_box = Box([])

        found_key = main_box.look_for_key()
        self.assertIsNone(found_key)


class LookForKeyRecursionTestCase(unittest.TestCase):
    """Тесты для поиска ключа в коробке с использованием рекурсии."""

    def test_key_in_main_box(self):
        """Тест нахождения ключа в основной коробке."""
        key = Item(ItemType.KEY)
        main_box = Box([key])

        found_key = main_box.look_for_key_recursion()
        self.assertIsNotNone(found_key)
        self.assertTrue(found_key.is_a_key())

    def test_key_in_inner_box(self):
        """Тест нахождения ключа во внутренней коробке."""
        key = Item(ItemType.KEY)
        inner_box = Box([key])
        main_box = Box([Item(ItemType.ITEM), inner_box])

        found_key = main_box.look_for_key_recursion()
        self.assertIsNotNone(found_key)
        self.assertTrue(found_key.is_a_key())

    def test_key_not_found(self):
        """Тест, когда ключ не найден."""
        main_box = Box([Item(ItemType.ITEM), Box([Item(ItemType.ITEM)])])

        found_key = main_box.look_for_key_recursion()
        self.assertIsNone(found_key)

    def test_multiple_boxes_with_key(self):
        """Тест нахождения ключа в нескольких коробках."""
        key = Item(ItemType.KEY)
        inner_box1 = Box([Item(ItemType.ITEM)])
        inner_box2 = Box([key])
        main_box = Box([inner_box1, inner_box2])

        found_key = main_box.look_for_key_recursion()
        self.assertIsNotNone(found_key)
        self.assertTrue(found_key.is_a_key())

    def test_empty_box(self):
        """Тест, когда коробка пустая."""
        main_box = Box([])

        found_key = main_box.look_for_key_recursion()
        self.assertIsNone(found_key)


class FactorialTestCase(unittest.TestCase):
    """Тесты для функции вычисления факториала."""

    def test_factorial(self):
        """Тесты для различных значений факториала."""
        self.assertEqual(fact(2), 2)
        self.assertEqual(fact(3), 6)
        self.assertEqual(fact(5), 120)


class SumArrayTestCase(unittest.TestCase):
    """
    Тестовый класс для проверки функций суммирования массива.
    """

    def test_sum_array(self):
        """
        Тестирует функцию sum_arr на различных входных данных.
        """
        self.assertEqual(sum_arr([1, 2, 3, 4]), 10)
        self.assertEqual(sum_arr([]), 0)
        self.assertEqual(sum_arr([1]), 1)

    def test_sum_array_recursion(self):
        """
        Тестирует рекурсивную функцию sum_arr_recursive на различных входных данных.
        """
        self.assertEqual(sum_arr_recursive([1, 2, 3, 4]), 10)
        self.assertEqual(sum_arr_recursive([]), 0)
        self.assertEqual(sum_arr_recursive([1]), 1)


if __name__ == '__main__':
    unittest.main()
