# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

"""Console-Based Simple Calculator."""


# -----------------------------------------------------------------------------
# Arithmetic operations
# -----------------------------------------------------------------------------
def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b rounded to 2 decimals, or None if b is zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Return the remainder of a / b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def format_number(value):
    """Show 13 instead of 13.0 for whole numbers."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return f"{value:g}"


def read_number(prompt):
    """Read a number from the user, re-prompting until valid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a number.")


def display_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


# -----------------------------------------------------------------------------
# Main loop
# -----------------------------------------------------------------------------
OPERATIONS = {
    "1": ("+", add),
    "2": ("-", subtract),
    "3": ("*", multiply),
    "4": ("/", divide),
    "5": ("%", modulus),
    "6": ("**", power),
}


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice. Please select a number from 1 to 7.")
            continue

        symbol, operation = OPERATIONS[choice]
        a = read_number("Enter first number : ")
        b = read_number("Enter second number: ")

        try:
            result = operation(a, b)
        except (OverflowError, ValueError):
            print("Error: The result is too large or undefined.")
            continue

        if result is None:
            if symbol == "/":
                print("Error: Cannot divide by zero.")
            else:
                print("Error: Cannot take the modulus of zero.")
            continue

        print(f"Result: {format_number(a)} {symbol} {format_number(b)} "
              f"= {format_number(result)}")


if __name__ == "__main__":
    main()