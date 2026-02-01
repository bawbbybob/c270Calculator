"""
Unit tests for the Calculator class using pytest.
"""
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Fixture to provide a Calculator instance."""
    return Calculator()


# 1. Test for Addition
def test_addition(calc):
    assert calc.add(2, 3) == 5


# 2. Test for Division by Zero
def test_division_by_zero(calc):
    assert calc.divide(10, 0) == "Error: Division by zero is not allowed."


# 3. Test for Floating-Point Precision
def test_floating_point_precision(calc):
    assert calc.add(0.1, 0.2) == pytest.approx(0.3, abs=1e-9)


# 4. Test for Large Numbers
def test_large_numbers(calc):
    assert calc.multiply(999999999, 999999999) == 999999998000000001


# 5. Test for Negative Results
def test_negative_results(calc):
    assert calc.add(-10, 5) == -5
    assert calc.subtract(5, 10) == -5


# 6. Test for Combined Operations
def test_combined_operations(calc):
    assert calc.subtract(calc.add(5, 3), 2) == 6


# 7. Test for Invalid Input Handling
def test_invalid_input(calc):
    with pytest.raises(TypeError):
        calc.add("a", 2)

    with pytest.raises(TypeError):
        calc.multiply("abc", 2)