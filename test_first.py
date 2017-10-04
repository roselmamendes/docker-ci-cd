import unittest
from calculator import sum

class TestFirst(unittest.TestCase):
    def test_should_sum_two_numbers(self):
        self.assertEqual(5, sum(2,3))
