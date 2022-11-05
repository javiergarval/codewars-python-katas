import unittest

from katas.multiples_of_3_and_5 import multiples_of_3_and_5


class Test(unittest.TestCase):
    def test_should_return_3_when_number_is_4(self):
        self.assertEqual(multiples_of_3_and_5(4), 3)

    def test_should_return_8_when_number_is_6(self):
        self.assertEqual(multiples_of_3_and_5(6), 8)

    def test_should_return_60_when_number_is_16(self):
        self.assertEqual(multiples_of_3_and_5(16), 60)

    def test_should_return_0_when_number_is_3(self):
        self.assertEqual(multiples_of_3_and_5(3), 0)

    def test_should_return_3_when_number_is_5(self):
        self.assertEqual(multiples_of_3_and_5(5), 3)

    def test_should_return_45_when_number_is_15(self):
        self.assertEqual(multiples_of_3_and_5(15), 45)

    def test_should_return_0_when_number_is_0(self):
        self.assertEqual(multiples_of_3_and_5(0), 0)

    def test_should_return_0_when_number_is_minus_1(self):
        self.assertEqual(multiples_of_3_and_5(-1), 0)

    def test_should_return_23_when_number_is_10(self):
        self.assertEqual(multiples_of_3_and_5(10), 23)

    def test_should_return_78_when_number_is_20(self):
        self.assertEqual(multiples_of_3_and_5(20), 78)

    def test_should_return_9168_when_number_is_200(self):
        self.assertEqual(multiples_of_3_and_5(200), 9168)
