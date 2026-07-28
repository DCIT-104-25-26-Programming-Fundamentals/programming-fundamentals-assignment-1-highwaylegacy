# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

"""Fibonacci Sequence Generator (iterative — no recursion)."""


# -----------------------------------------------------------------------------
# PART A — Print the first N terms
# -----------------------------------------------------------------------------
def generate_fibonacci(n):
    """Return a list with the first n Fibonacci numbers, or None if n < 1."""
    if n < 1:
        return None
    sequence = []
    current, nxt = 0, 1
    for _ in range(n):
        sequence.append(current)
        current, nxt = nxt, current + nxt
    return sequence


def print_fibonacci(n):
    """Print the first n Fibonacci terms on one line."""
    sequence = generate_fibonacci(n)
    if sequence is None:
        print("Error: N must be a positive integer.")
        return
    print("Fibonacci sequence:", " ".join(str(v) for v in sequence))


# -----------------------------------------------------------------------------
# PART B — Check membership in the sequence
# -----------------------------------------------------------------------------
def is_fibonacci(number):
    """Return True if number appears in the Fibonacci sequence."""
    if number < 0:
        return False
    current, nxt = 0, 1
    while current < number:
        current, nxt = nxt, current + nxt
    return current == number


def check_fibonacci(number):
    """Print whether number is a Fibonacci number."""
    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


# -----------------------------------------------------------------------------
# Menu
# -----------------------------------------------------------------------------
def main():
    while True:
        print("\n========= FIBONACCI SEQUENCE =========")
        print("1. Print the first N terms")
        print("2. Check if a number is a Fibonacci number")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            try:
                n = int(input("How many terms? "))
            except ValueError:
                print("Error: N must be a positive integer.")
                continue
            print_fibonacci(n)

        elif choice == "2":
            try:
                number = int(input("Enter a number to check: "))
            except ValueError:
                print("Error: Please enter a valid whole number.")
                continue
            check_fibonacci(number)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2 or 3.")


if __name__ == "__main__":
    main()