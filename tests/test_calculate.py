import unittest

from CI_CD_sample.calculate import sum_nums, multiple_nums

# from math_operations import sum, multiple

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

    def test_multiple(self):
        # Test when both numbers are positive
        self.assertEqual(multiple_nums(2, 3), 6)
        # Test when one number is negative
        self.assertEqual(multiple_nums(-2, 4), -8)
        # Test when both numbers are negative
        self.assertEqual(multiple_nums(-3, -7), 21)
        # Test when one number is zero
        self.assertEqual(multiple_nums(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
