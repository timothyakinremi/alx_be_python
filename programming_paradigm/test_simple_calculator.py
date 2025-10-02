# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---- Addition Tests ----
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    # ---- Subtraction Tests ----
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    # ---- Multiplication Tests ----
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(4, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    # ---- Division Tests ----
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_mixed_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))


if __name__ == "__main__":
    unittest.main()
