import math

"""Calculator logic module."""


class Calculator:
    """Basic arithmetic operations."""

    def add(self, left, right):
        """Adds two numbers."""
        return left + right

    def subtract(self, left, right):
        """Subtracts the second number from the first."""
        return left - right

    def multiply(self, left, right):
        """Multiplies both numbers."""
        return left * right

    def divide(self, left, right):
        """Divides the first number by the second. Returns error if dividing by 0."""
        if right == 0:
            return "Error: Division by zero is not allowed."
        return left / right
