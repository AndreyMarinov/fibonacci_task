'''Testing the fibonacci modul for printing the first 10 Fibonacci numbers
and one modul with calculating them'''

import unittest

from src.fibonacci_task import get_fibonacci_num, get_fibonacci_first_ten_numbers



class TestFibonacciCalculation(unittest.TestCase):
    '''Testing modul that calculates Fibonacci values'''


    def test_fibonacci_calculating_with_zero(self):
        '''Testing the calculation with zero'''
        self.assertEqual(get_fibonacci_num(0),0)


    def test_fibonacci_calculating_with_one(self):
        '''Testing the calculation with one'''
        self.assertEqual(get_fibonacci_num(1),1)


    def test_fibonacci_calculating_with_nine(self):
        '''Testing the calculation with nine'''
        self.assertEqual(get_fibonacci_num(9),34)


    def test_fibonacci_calculating_with_ten(self):
        '''Testing the calculation with ten'''
        self.assertEqual(get_fibonacci_num(10),55)


class TestFibonacciFirstTenNumbers(unittest.TestCase):
    '''Testing modul that print the first 10 Fibonacci numbers'''


    def test_fibonacci_first_ten_numbers_function(self):
        '''Testing the modul with the first 10 numbers of Fibonacci'''
        expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        received_result = get_fibonacci_first_ten_numbers()          #pylint:disable = no-value-for-parameter
        self.assertEqual(expected_result, received_result)


if __name__ == '__main__':
    unittest.main()
