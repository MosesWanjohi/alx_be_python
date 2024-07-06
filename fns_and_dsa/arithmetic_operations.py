def perform_operation(num1, num2, operation):
    """Performs basic arithmetic operations."""
    if operation == "add":
        result = num1 + num2
        return result
    elif operation == "subtract":
        result = num1 - num2
        return result
    elif operation == "multiply":
        result = num1 * num2
        return result
    elif operation == "divide":
        if num2 == 0:
            result = ("You cannot divide by zero")
        else:
            result = num1 / num2
            return result
    else:
        result = "Invalid operation"
        return result

num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))
operation = input("Enter the operation {add, subtract, multiply, divide}")
result = perform_operation(num1, num2, operation)
print(f"Result: {result}")
