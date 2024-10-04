#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:number>')
def count(number):
    numbers_in_range = '\n'.join(str(num) for num in range(number)) + '\n'
    return f'{numbers_in_range}'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        if num2 == 0:
            return "Dividing a number by zero is not allowed."
        else:
            return str(num1 / num2)
    elif operation == "%":
        if num2 == 0:
            return "Computing the modulus of a number by zero is not allowed."
        else:
            return str(num1 % num2)
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
