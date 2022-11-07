import unittest

from katas.battleship_field_validator import validate_battlefield


class Test(unittest.TestCase):
    def test_should_be_true_when_all_ships_are_placed_correctly(self):
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

    def test_should_be_false_when_there_are_more_than_4_submarines(self):
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

    def test_should_be_false_when_there_are_more_than_3_destroyers(self):
        battle_field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]]
        self.assertFalse(validate_battlefield(battle_field))

    def test_should_be_false_when_there_are_more_than_2_cruisers(self):
        battle_field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]]
        self.assertFalse(validate_battlefield(battle_field))

    def test_should_be_false_when_there_is_more_than_1_battleship(self):
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

    def test_should_be_false_if_ships_are_in_contact(self):
        battle_field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(validate_battlefield(battle_field))
