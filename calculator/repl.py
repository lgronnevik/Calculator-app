from calculator.operations import add, subtract, multiply, divide

def main():
    print("Welcome to your calculator!")
    print("Type 'add', 'subtract', 'multiply', 'divide' to perform operations.")
    print("Type 'quit' to exit.")

    while True:
        command = input("\nEnter operation: ").strip().lower()
        if command == "quit":
            print("Goodbye!")
            break

        if command not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter numeric values.")
            continue

        try:
            if command == "add":
                result = add(a, b)
            elif command == "subtract":
                result = subtract(a, b)
            elif command == "multiply":
                result = multiply(a, b)
            elif command == "divide":
                result = divide(a, b)
            print("Result:", result)
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
