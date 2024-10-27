import unittest

import os

from CI_CD_sample.calculate import sum_nums, get_minimum

class Test_Calculate(unittest.TestCase):

    def test_sum_nums(self):
        # Test when both numbers are positive
        self.assertEqual(sum_nums(2, 3), 5)
        # Test when one number is negative
        self.assertEqual(sum_nums(-1, 5), 4)
        # Test when both numbers are negative
        self.assertEqual(sum_nums(-3, -7), -10)
        # Test when both numbers are zero
        self.assertEqual(sum_nums(0, 0), 0)

    def test_get_minimum_with_non_empty_list(self):
        # Test with a regular list
        self.assertEqual(get_minimum([5, 3, 9, 1, 4]), 1)
        # Test with a list of negative numbers
        self.assertEqual(get_minimum([-5, -3, -9, -1]), -9)
        # Test with a list of one element
        self.assertEqual(get_minimum([7]), 7)

    def test_get_minimum_with_empty_list(self):
        # Test with an empty list and expect a RuntimeError
        with self.assertRaises(RuntimeError):
            get_minimum([])

if __name__ == '__main__':
    unittest.main()
