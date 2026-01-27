from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""

    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        operation = request.form.get('operation')

        if operation == 'add':
            result = calc.add(num1, num2)

        elif operation == 'subtract':
            result = calc.subtract(num1, num2)

        elif operation == 'multiply':
            result = calc.multiply(num1, num2)

        elif operation == 'divide':
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = calc.divide(num1, num2)

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
