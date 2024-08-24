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


class TestItem(unittest.TestCase):

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

    def test_is_a_box(self):
        box = Item(ItemType.Box)
        self.assertTrue(box.is_a_box())
        self.assertFalse(box.is_a_key())
        self.assertFalse(box.is_a_item())

    def test_is_a_key(self):
        key = Item(ItemType.Key)
        self.assertTrue(key.is_a_key())
        self.assertFalse(key.is_a_box())
        self.assertFalse(key.is_a_item())

    def test_is_a_item(self):
        item = Item(ItemType.Item)
        self.assertTrue(item.is_a_item())
        self.assertFalse(item.is_a_box())
        self.assertFalse(item.is_a_key())

    def test_get_items(self):
        key = Item(ItemType.Key)
        item = Item(ItemType.Item)
        box = Box([key, item])

        items = box.get_items()
        self.assertEqual(len(items), 2)
        self.assertIs(items[0], key)
        self.assertIs(items[1], item)


class LookForKeyTestCase(unittest.TestCase):

    def test_key_in_main_box(self):
        key = Item(ItemType.Key)
        main_box = Box([key])

        found_key = main_box.look_for_key()
        self.assertIsNotNone(found_key)
        self.assertTrue(found_key.is_a_key())

    def test_key_in_inner_box(self):
        key = Item(ItemType.Key)
        inner_box = Box([key])
        main_box = Box([Item(ItemType.Item), inner_box])

        found_key = main_box.look_for_key()
        self.assertIsNotNone(found_key)
        self.assertTrue(found_key.is_a_key())

    def test_key_not_found(self):
        main_box = Box([Item(ItemType.Item), Box([Item(ItemType.Item)])])

        found_key = main_box.look_for_key()
        self.assertIsNone(found_key)

    def test_multiple_boxes_with_key(self):
        key = Item(ItemType.Key)
        inner_box1 = Box([Item(ItemType.Item)])
        inner_box2 = Box([key])
        main_box = Box([inner_box1, inner_box2])

        found_key = main_box.look_for_key()
        self.assertIsNotNone(found_key)
        self.assertTrue(found_key.is_a_key())

    def test_empty_box(self):
        main_box = Box([])

        found_key = main_box.look_for_key()
        self.assertIsNone(found_key)


if __name__ == '__main__':
    unittest.main()
