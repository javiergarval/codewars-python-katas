import unittest

from katas.sum_without_highest_and_lowest_number import sum_without_highest_and_lowest_number


class Test(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(sum_without_highest_and_lowest_number(None), 0)
        self.assertEqual(sum_without_highest_and_lowest_number([]), 0)

    def test_one_test_cases(self):
        self.assertEqual(sum_without_highest_and_lowest_number([3]), 0)
        self.assertEqual(sum_without_highest_and_lowest_number([-3]), 0)

    def test_two_test_cases(self):
        self.assertEqual(sum_without_highest_and_lowest_number([3, 5]), 0)
        self.assertEqual(sum_without_highest_and_lowest_number([-3, -5]), 0)

    def test_real_test_cases(self):
        self.assertEqual(sum_without_highest_and_lowest_number([6, 2, 1, 8, 10]), 16)
        self.assertEqual(sum_without_highest_and_lowest_number([6, 0, 1, 10, 10]), 17)
        self.assertEqual(sum_without_highest_and_lowest_number([-6, -20, -1, -10, -12]), -28)
        self.assertEqual(sum_without_highest_and_lowest_number([-6, 20, -1, 10, -12]), 3)
