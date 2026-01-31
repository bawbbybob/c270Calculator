import math

class Calculator:
    def add(self, a, b):
        """Adds two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtracts the second number from the first."""
        return a - b
    
    def multiply(self, a, b):
        """Multiplies both numbers."""
        return a * b

    def divide(self, a, b):
        """Divides the first number by the second. Returns error if dividing by 0."""
        if b == 0:
            return "Error: Division by Zero"
        return a / b

    def power(self, a, b):
        """Returns 'a' raised to the power of 'b'."""
        return a ** b

    def radical(self, a):
        """Returns the square root of 'a'. Returns error for negative numbers."""
        if a < 0:
            return "Error: Negative Radical"
        return math.sqrt(a)


# Example usage
if __name__ == "__main__":
    calc = Calculator()
    
    # Addition
    result_add = calc.add(10, 5)
    print(f"10 + 5 = {result_add}")
    
    # Subtraction
    result_sub = calc.subtract(10, 5)
    print(f"10 - 5 = {result_sub}")

    # Multiplication
    result_mul = calc.multiply(10, 5)
    print(f"10 * 5 = {result_mul}")
    
    # Division
    result_div = calc.divide(10, 5)
    print(f"10 / 5 = {result_div}")
    
    # Division by zero
    result_div_zero = calc.divide(10, 0)
    print(f"10 / 0 = {result_div_zero}")

    # Power Test (e.g., 2 to the power of 3)
    print(f"2^3 = {calc.power(2, 3)}") # Expected: 8
    
    # Radical Test (e.g., square root of 25)
    print(f"√25 = {calc.radical(25)}") # Expected: 5.0
    
    # Negative Radical Test
    print(f"√-1 = {calc.radical(-1)}") # Expected: Error message