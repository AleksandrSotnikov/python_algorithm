import unittest

from codes.binary_search import binary_search
from codes.binary_search import binary_search_count_operation


class MyTestCase(unittest.TestCase):
    def test_something(self):
        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(binary_search(int_list, 25), None)
        self.assertEqual(binary_search(int_list, 12), 11)
        self.assertEqual(binary_search_count_operation(int_list, 5), 2)
        self.assertEqual(binary_search_count_operation(int_list, 6), 4)


if __name__ == '__main__':
    unittest.main()
