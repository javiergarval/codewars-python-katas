import unittest

from katas.evaluate_mathematical_expression import evaluate_mathematical_expression


class Test(unittest.TestCase):
    def test_evaluate_mathematical_expression(self):
        self.assertEqual(evaluate_mathematical_expression("1 + 1"), 2)
        self.assertEqual(evaluate_mathematical_expression("8/16"), 0.5),
        self.assertEqual(evaluate_mathematical_expression("3 -(-1)"), 4),
        self.assertEqual(evaluate_mathematical_expression("2 + -2"), 0),
        self.assertEqual(evaluate_mathematical_expression("10- 2- -5"), 13),
        self.assertEqual(evaluate_mathematical_expression("(((10)))"), 10),
        self.assertEqual(evaluate_mathematical_expression("3 * 5"), 15),
        self.assertEqual(evaluate_mathematical_expression("-7 * -(6 / 3)"), 14)
