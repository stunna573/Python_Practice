"""A simple command-line calculator."""


def calculate(first, operator, second):
    """Calculate a result for one of the supported arithmetic operators."""
    operations = {
        "+": lambda: first + second,
        "-": lambda: first - second,
        "*": lambda: first * second,
        "/": lambda: first / second,
    }
    if operator not in operations:
        raise ValueError("Choose one of: +, -, *, /.")
    if operator == "/" and second == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return operations[operator]()


def main():
    print("Python Practice Calculator")
    try:
        first = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))
        result = calculate(first, operator, second)
    except ValueError as error:
        print("Invalid input:", error)
    except ZeroDivisionError as error:
        print("Calculation error:", error)
    else:
        print("Result:", result)


if __name__ == "__main__":
    main()
