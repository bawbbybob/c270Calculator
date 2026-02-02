"""Flask web app for the calculator UI."""
from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render calculator page and process operations."""
    result = None

    if request.method == 'POST':
        try:
            # Get the operation and first number
            operation = request.form.get('operation')
            num1 = float(request.form.get('num1'))

            # Handle the Radical (Special case: only needs one number)
            if operation == 'radical':
                result = calc.radical(num1)

            else:
                # All other operations need the second number
                num2 = float(request.form.get('num2'))

                if operation == 'add':
                    result = calc.add(num1, num2)
                elif operation == 'subtract':
                    result = calc.subtract(num1, num2)
                elif operation == 'multiply':
                    result = calc.multiply(num1, num2)
                elif operation == 'divide':
                    result = calc.divide(num1, num2)
                elif operation == 'power':
                    result = calc.power(num1, num2)

        except (ValueError, TypeError):
            result = "Error: Invalid Input"

    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
