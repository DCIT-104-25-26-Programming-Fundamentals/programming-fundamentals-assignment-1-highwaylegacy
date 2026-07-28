# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

"""Multiplication Table Generator."""

LIMIT = 12          # tables run from 1 to 12
SEPARATOR = "-" * 27


# -----------------------------------------------------------------------------
# PART A — Single table
# -----------------------------------------------------------------------------
def print_single_table(number):
    """Print the multiplication table for `number` from 1 to LIMIT."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, LIMIT + 1):
        product = number * i
        print(f"{number}  x  {str(i).ljust(2)} =  {product}")


# -----------------------------------------------------------------------------
# PART B — Tables from 1 to N
# -----------------------------------------------------------------------------
def print_all_tables(n):
    """Print every multiplication table from 1 to n, separated by a line."""
    for number in range(1, n + 1):
        print_single_table(number)
        if number != n:
            print(SEPARATOR)


# -----------------------------------------------------------------------------
# Menu
# -----------------------------------------------------------------------------
def read_positive_int(prompt):
    """Return a positive integer from the user, or None if the input is bad."""
    try:
        value = int(input(prompt))
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return None
    if value <= 0:
        print("Error: The number must be a positive integer.")
        return None
    return value


def main():
    while True:
        print("\n====== MULTIPLICATION TABLE GENERATOR ======")
        print("1. Table for a single number")
        print("2. Tables from 1 to N")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            number = read_positive_int("Enter a number: ")
            if number is not None:
                print()
                print_single_table(number)

        elif choice == "2":
            n = read_positive_int("Enter N: ")
            if n is not None:
                print()
                print_all_tables(n)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2 or 3.")


if __name__ == "__main__":
    main()