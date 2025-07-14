# test_simple_calculator.py

import unittest
# Assuming simple_calculator.py is in the same directory or accessible via PYTHONPATH
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method runs."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method with various valid inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(-5, -10), -15)

    def test_subtract(self):
        """Test the subtract method with various valid inputs."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(10, 20), -10)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)

    def test_multiply(self):
        """Test the multiply method with various valid inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(-4, -5), 20)

    def test_divide(self):
        """Test the divide method with various valid inputs and edge cases."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(5, -2), -2.5)

    def test_divide_by_zero(self):
        """Test the divide method when the denominator is zero."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Even 0/0 should return None as per SimpleCalculator's logic

# This allows running tests directly from the command line
if __name__ == '__main__':
    unittest.main()
