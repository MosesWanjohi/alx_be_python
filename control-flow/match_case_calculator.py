num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("choose the operation (+, -, *, /): ")
match operation:
    case "+":
        print(f"The result is: ", int(num1) + int(num2))
    case "-":
        print(f"The result is: ", int(num1) - int(num2))
    case "*":
        print(f"The result is: ", int(num1) * int(num2))
    case "/":
            if int(input("Enter the second number: ")) >= 1:
                print(f"The result is: ", int(num1) / int(num2))
            else:
                print("Cannot divide by zero")
