from unittest import TestCase
from katas.reverse_string import reverse_string


class Test(TestCase):
    def test_reverse_string(self):
        assert reverse_string('world') == 'dlrow'
        assert reverse_string('hello') == 'olleh'
        assert reverse_string('') == ''
        assert reverse_string('h') == 'h'
