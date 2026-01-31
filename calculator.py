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