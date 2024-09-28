while True:
    num1 = input("Enter the first number (or type 'exit' to quit): ")
    if num1.lower() == 'exit':
        break
    num2 = input("Enter the second number: ")
    if num2.lower() == 'exit':
        break
    operation = input("Enter an operation (+, -, *, /): ")
    if operation.lower() == 'exit':
        break
    num1 = float(num1)
    num2 = float(num2)
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"
    print(f"The result is: {result}")
while True:
    num1 = input("Enter the first number (or type 'exit' to quit): ")
    if num1.lower() == 'exit':
        break
    num2 = input("Enter the second number: ")
    num1 = float(num1)
    num2 = float(num2)
    operation = input("Enter an operation (+, -, *, /): ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    print(f"The result is: {result}")
