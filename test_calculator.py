import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Standard setup to initialize the calculator instance before each test."""
        self.calc = Calculator()

    # --- Version 1 Tests ---
    def test_addition(self):
        # Test case: 2 + 3 = 5
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_division_by_zero(self):
        # Test case: Ensure error message matches the logic in calculator.py
        # Note: Updated string to match your calculator.py: "Error: Division by Zero"
        self.assertEqual(self.calc.divide(10, 0), "Error: Division by Zero")

    # --- Version 2 Tests (New Features) ---
    def test_power(self):
        """Tests the power (exponent) functionality."""
        # Case: 2 to the power of 3 = 8
        self.assertEqual(self.calc.power(2, 3), 8)
        # Case: Any number to the power of 0 = 1
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_radical(self):
        """Tests the square root functionality."""
        # Case: Square root of 25 = 5.0
        self.assertEqual(self.calc.radical(25), 5.0)
        # Case: Square root of 0 = 0.0
        self.assertEqual(self.calc.radical(0), 0.0)

    def test_negative_radical(self):
        """Security/Error Handling: Tests square root of a negative number."""
        # Based on your calculator.py logic for Version 2
        self.assertEqual(self.calc.radical(-1), "Error: Negative Radical")

if __name__ == '__main__':
    unittest.main()