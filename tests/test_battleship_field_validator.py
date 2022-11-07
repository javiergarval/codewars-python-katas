import unittest

from katas.battleship_field_validator import validate_battlefield


class Test(unittest.TestCase):
    def test_battleship_field_validator(self):
        battle_field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(validate_battlefield(battle_field))

    def test_should_be_false(self):
        battle_field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(validate_battlefield(battle_field))

    def test_should_not_return_out_of_range(self):
        battle_field = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]
        self.assertFalse(validate_battlefield(battle_field))

    def test_should_be_true(self):
        battle_field = [[0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(validate_battlefield(battle_field))
