import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # 1. Test for Addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    # 2. Test for Division by Zero
    def test_division_by_zero(self):
        self.assertEqual(self.calc.divide(10, 0), "Error: Division by zero is not allowed.")

    # 3. Test for Floating-Point Precision
    def test_floating_point_precision(self):
        self.assertEqual(self.calc.add(0.1, 0.2), 0.3, places=9)  # ensures floating point precision

    # 4. Test for Large Numbers
    def test_large_numbers(self):
        self.assertEqual(self.calc.multiply(999999999, 999999999), 999999998000000001)

    # 5. Test for Negative Results
    def test_negative_results(self):
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    # 6. Test for Combined Operations
    def test_combined_operations(self):
        self.assertEqual(self.calc.subtract(self.calc.add(5, 3), 2), 6)

    # 7. Test for Invalid Input Handling
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.calc.add("a", 2)
        
        with self.assertRaises(TypeError):
            self.calc.multiply("abc", 2)

if __name__ == '__main__':
    unittest.main()
