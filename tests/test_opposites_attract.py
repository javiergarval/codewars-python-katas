import unittest

from katas.opposites_attract import opposites_attract


class Test(unittest.TestCase):
    def test_opposites_attract(self):
        self.assertTrue(opposites_attract(1, 4))
        self.assertFalse(opposites_attract(2, 2))
        self.assertTrue(opposites_attract(0, 1))
        self.assertFalse(opposites_attract(0, 0))
