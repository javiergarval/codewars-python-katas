import unittest

from katas.moving_zeros_to_the_end import moving_zeros_to_the_end


class Test(unittest.TestCase):
    def test_moving_zeros_to_the_end(self):
        self.assertEqual(moving_zeros_to_the_end(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        self.assertEqual(moving_zeros_to_the_end(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(moving_zeros_to_the_end([0, 0]), [0, 0])
        self.assertEqual(moving_zeros_to_the_end([0]), [0])
        self.assertEqual(moving_zeros_to_the_end([]), [])
