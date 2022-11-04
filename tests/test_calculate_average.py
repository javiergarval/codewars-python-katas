import unittest

from katas.calculate_average import calculate_average


class Test(unittest.TestCase):
    def test_real_case(self):
        self.assertEqual(calculate_average([1, 2, 3]), 2)

    def test_empty_case(self):
        self.assertEqual(calculate_average(None), 0)
        self.assertEqual(calculate_average([]), 0)
