# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

"""Array Statistics Calculator (no built-in sum/max/min)."""


def calculate_sum(numbers):
    """Return the sum of the list using a loop."""
    total = 0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers):
    """Return the arithmetic mean of the list."""
    if not numbers:
        return None
    count = 0
    for _ in numbers:
        count += 1
    return calculate_sum(numbers) / count


def find_maximum(numbers):
    """Return the largest value in the list."""
    if not numbers:
        return None
    largest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
    return largest


def find_minimum(numbers):
    """Return the smallest value in the list."""
    if not numbers:
        return None
    smallest = numbers[0]
    for value in numbers:
        if value < smallest:
            smallest = value
    return smallest


def format_number(value):
    """Print 5 instead of 5.0 for whole numbers."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def read_numbers(n):
    """Prompt the user for n numbers and return them as a list."""
    numbers = []
    for i in range(1, n + 1):
        while True:
            try:
                numbers.append(float(input(f"Enter number {i}: ")))
                break
            except ValueError:
                print("  Invalid input. Please enter a number.")
    return numbers


def main():
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = read_numbers(n)

    print("\nResults:")
    print(f"Sum:     {format_number(calculate_sum(numbers))}")
    print(f"Average: {round(calculate_average(numbers), 2)}")
    print(f"Maximum: {format_number(find_maximum(numbers))}")
    print(f"Minimum: {format_number(find_minimum(numbers))}")


if __name__ == "__main__":
    main()