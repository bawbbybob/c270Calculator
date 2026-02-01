import math

"""Calculator logic module."""


class Calculator:
    """Basic arithmetic operations."""

    def add(self, left, right):
        """Adds two numbers."""
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return left + right

    def subtract(self, left, right):
        """Subtracts the second number from the first."""
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return left - right

    def multiply(self, left, right):
        """Multiplies both numbers."""
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return left * right

    def divide(self, left, right):
        """Divides the first number by the second. Returns error if dividing by 0."""
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise TypeError("Both arguments must be numbers")
        if right == 0:
            return "Error: Division by zero is not allowed."
        return left / right
