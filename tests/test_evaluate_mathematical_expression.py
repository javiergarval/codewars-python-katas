import unittest

from katas.evaluate_mathematical_expression import evaluate_mathematical_expression


class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(evaluate_mathematical_expression("1 + 1"), 2)

    def test_division(self):
        self.assertEqual(evaluate_mathematical_expression("8/16"), 0.5),

    def test_double_negation(self):
        self.assertEqual(evaluate_mathematical_expression("3 -(-1)"), 4),

    def test_addition_and_subtraction(self):
        self.assertEqual(evaluate_mathematical_expression("2 + -2"), 0),

    def test_subtraction_and_double_negation(self):
        self.assertEqual(evaluate_mathematical_expression("10- 2- -5"), 13),

    def test_nested_parenthesis(self):
        self.assertEqual(evaluate_mathematical_expression("(((10)))"), 10),

    def test_multiplication(self):
        self.assertEqual(evaluate_mathematical_expression("3 * 5"), 15),

    def test_parenthesis_priority(self):
        self.assertEqual(evaluate_mathematical_expression("-7 * -(6 / 3)"), 14)
