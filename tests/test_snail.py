import unittest

from katas.snail import snail


class Test(unittest.TestCase):
    def test_3_by_3_ordered_matrix(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(snail(array), expected)

    def test_3_by_3_unordered_matrix(self):
        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(snail(array), expected)

    def test_4_by_4_unordered_matrix(self):
        array = [
            [1, 2, 3, 1],
            [4, 5, 6, 4],
            [7, 8, 9, 7],
            [7, 8, 9, 7]]
        expected = [1, 2, 3, 1, 4, 7, 7, 9, 8, 7, 7, 4, 5, 6, 9, 8]
        self.assertEqual(snail(array), expected)
