import unittest
from variations import combinations_var, input_combination


class TestCase(unittest.TestCase):

    def test_func(self):
        result = combinations_var(input_combination())
        self.assertEqual(result, ['abcd', 'a.bcd', 'ab.cd', 'a.b.cd', 'abc.d', 'a.bc.d', 'ab.c.d', 'a.b.c.d'])
