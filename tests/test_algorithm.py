import unittest

from codes.binary_search import *
from codes.recursion.item import *
from codes.selection_sort import *


class AlgorithmTestCase(unittest.TestCase):
    def test_binary_search(self):
        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(binary_search(int_list, 25), None)
        self.assertEqual(binary_search(int_list, 12), 11)

    def test_binary_search_count_operation(self):
        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(binary_search_count_operation(int_list, 5), 2)
        self.assertEqual(binary_search_count_operation(int_list, 6), 4)

    def test_finder_smallest_number_index(self):
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(finder_smallest_number_index(int_list), 3)
        self.assertEqual(finder_smallest_number_index(none_list), None)

    def test_finder_largest_number_index(self):
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(finder_largest_number_index(int_list), 0)
        self.assertEqual(finder_largest_number(none_list), None)

    def test_finder_smallest_number(self):
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(finder_smallest_number(int_list), 1)
        self.assertEqual(finder_smallest_number(none_list), None)

    def test_finder_largest_number(self):
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(finder_largest_number(int_list), 6)
        self.assertEqual(finder_largest_number(none_list), None)

    def test_selection_sort_ascending(self):
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(selection_sort_ascending(none_list), [])
        self.assertEqual(selection_sort_ascending(int_list), [1, 2, 3, 4, 5, 6])

    def test_selection_sort_descending(self):
        int_list = [6, 4, 3, 1, 2, 5]
        none_list = []
        self.assertEqual(selection_sort_descending(none_list), [])
        self.assertEqual(selection_sort_descending(int_list), [6, 5, 4, 3, 2, 1])


class TestItemTypes(unittest.TestCase):

    def test_item_creation(self):
        item = ItemFactory.create_item(ItemType.Item)
        self.assertEqual(item.get_item_type(), ItemType.Item)
        self.assertIsInstance(item, Item)

    def test_key_creation(self):
        key = ItemFactory.create_item(ItemType.Key)
        self.assertEqual(key.get_item_type(), ItemType.Key)
        self.assertIsInstance(key, Key)

    def test_box_creation_without_items(self):
        box = ItemFactory.create_item(ItemType.Box)
        self.assertEqual(box.get_item_type(), ItemType.Box)
        self.assertIsInstance(box, Box)
        self.assertEqual(len(box.items), 0)

    def test_box_creation_with_items(self):
        key = ItemFactory.create_item(ItemType.Key)
        item = ItemFactory.create_item(ItemType.Item)
        box = ItemFactory.create_item(ItemType.Box, [key, item])
        self.assertEqual(box.get_item_type(), ItemType.Box)
        self.assertIsInstance(box, Box)
        self.assertEqual(len(box.items), 2)
        self.assertIsInstance(box.items[0], Key)
        self.assertIsInstance(box.items[1], Item)

    def test_factory_returns_correct_types(self):
        key = ItemFactory.create_item(ItemType.Key)
        box = ItemFactory.create_item(ItemType.Box, [])
        item = ItemFactory.create_item(ItemType.Item)

        self.assertIsInstance(key, Key)
        self.assertIsInstance(box, Box)
        self.assertIsInstance(item, Item)


if __name__ == '__main__':
    unittest.main()
