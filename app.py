from flask import Flask, render_template, request
from calculator import Calculator # Importing the logic class you updated

app = Flask(__name__)
calc = Calculator()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None # Set to None so the result box only shows when needed

    if request.method == 'POST':
        try:
            # 1. Get the operation first to check if we need one or two numbers
            operation = request.form.get('operation')
            num1 = float(request.form.get('num1'))
            
            # 2. Handle the Radical (Special case: only needs one number)
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
                    # NEW Version 2 Function [cite: 17]
                    result = calc.power(num1, num2)

        except (ValueError, TypeError):
            # Security: Handle non-numeric inputs gracefully 
            result = "Error: Invalid Input"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    # Ensure the app is accessible within a Docker container
    app.run(host="0.0.0.0", port=8080)