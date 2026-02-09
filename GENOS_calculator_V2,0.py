import math

def calculator():
    print("Simple Calculator v2.0")
    print("Available operations:")
    print("+    : Addition")
    print("-    : Subtraction")
    print("*    : Multiplication")
    print("/    : Division")
    print("abs  : Absolute Value")
    print("sqrt : Square Root")
    print("Type 'exit' to quit\n")

    two_number_ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else "Error: Division by zero"
    }


    one_number_ops = {
        "abs": abs,
        "sqrt": lambda x: math.sqrt(x) if x >= 0 else "Error: Negative number"
    }

    while True:
        operation = input("Enter the operation: ").strip().lower()

        if operation == "exit":
            print("Exiting calculator. Goodbye!")
            break

        # One-number operations
        if operation in one_number_ops:
            try:
                num = float(input("Enter a number: "))
                result = one_number_ops[operation](num)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif operation in two_number_ops:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                result = two_number_ops[operation](a, b)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")

        else:
            print("Error: Invalid operation selected.")

        print()
 
calculator()
