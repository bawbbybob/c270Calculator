import unittest
from calculator import Calculator # This is the logic class you created

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        # Test case: 2 + 3 = 5
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_division_by_zero(self):
        # Test case: handling division by zero
        self.assertEqual(self.calc.divide(10, 0), "Error: Division by Zero")

if __name__ == '__main__':
    unittest.main()