"""Unit tests for selected portfolio functions."""

import unittest

from modules.math_helpers import digit_sum, find_max, find_min
from projects.calculator.calculator import calculate
from projects.sales.sales import calculate_total
from exceptions.exception_examples import InvalidMarksError, calculate_average


class MathHelperTests(unittest.TestCase):
    def test_find_max_and_min(self):
        self.assertEqual(find_max(3, 8), 8)
        self.assertEqual(find_min(3, 8), 3)

    def test_digit_sum(self):
        self.assertEqual(digit_sum(894), 21)

    def test_digit_sum_rejects_negative(self):
        with self.assertRaises(ValueError):
            digit_sum(-12)


class CalculatorTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate(8, "+", 2), 10)
        self.assertEqual(calculate(8, "-", 2), 6)
        self.assertEqual(calculate(8, "*", 2), 16)
        self.assertEqual(calculate(8, "/", 2), 4)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(8, "/", 0)

    def test_unknown_operator(self):
        with self.assertRaises(ValueError):
            calculate(8, "%", 2)


class SalesAndExceptionTests(unittest.TestCase):
    def test_sales_total(self):
        self.assertEqual(calculate_total(2500, 3), 7500)

    def test_average_and_invalid_marks(self):
        self.assertEqual(calculate_average(80, 100), 90)
        with self.assertRaises(InvalidMarksError):
            calculate_average(-1, 100)


if __name__ == "__main__":
    unittest.main()
