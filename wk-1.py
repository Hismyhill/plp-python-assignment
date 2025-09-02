# Basic Calculator Program

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

# Perform calculation
if operation == 'add':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == 'subtract':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == 'multiply':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == 'divide':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")