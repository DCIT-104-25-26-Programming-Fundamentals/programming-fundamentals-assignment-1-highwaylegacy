# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

"""Matrix Operations — transpose, addition and multiplication (pure Python)."""


# -----------------------------------------------------------------------------
# Input / output helpers
# -----------------------------------------------------------------------------
def read_int(prompt, minimum=1):
    """Read a whole number >= minimum from the user."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a whole number.")
            continue
        if value < minimum:
            print(f"  Value must be at least {minimum}.")
            continue
        return value


def read_matrix(rows, cols, name="Matrix"):
    """Read a rows x cols matrix, one row per line, values separated by spaces."""
    print(f"\nEnter values for {name} ({rows} x {cols}):")
    matrix = []
    for i in range(rows):
        while True:
            parts = input(f"Enter row {i + 1}: ").split()
            if len(parts) != cols:
                print(f"  Please enter exactly {cols} value(s).")
                continue
            try:
                row = [float(p) for p in parts]
            except ValueError:
                print("  All values must be numbers.")
                continue
            matrix.append(row)
            break
    return matrix


def format_value(value):
    """Show 5 instead of 5.0 for whole numbers."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return f"{value:g}"


def display_matrix(matrix, title=None):
    """Print a matrix as a neat, right-aligned grid."""
    if title:
        print(f"\n{title}")
    if not matrix:
        print("(empty matrix)")
        return
    text = [[format_value(v) for v in row] for row in matrix]
    width = 0
    for row in text:
        for cell in row:
            if len(cell) > width:
                width = len(cell)
    for row in text:
        print("  ".join(cell.rjust(width) for cell in row))


# -----------------------------------------------------------------------------
# PART A — Transpose
# -----------------------------------------------------------------------------
def transpose_matrix(matrix):
    """Return the transpose of an M x N matrix (result is N x M)."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


# -----------------------------------------------------------------------------
# PART B — Addition
# -----------------------------------------------------------------------------
def add_matrices(a, b):
    """Return the element-wise sum of two matrices of identical size."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


# -----------------------------------------------------------------------------
# PART C — Multiplication
# -----------------------------------------------------------------------------
def multiply_matrices(a, b):
    """Return the matrix product A (M x N) x B (N x P) -> M x P."""
    if len(a[0]) != len(b):
        return None
    m, n, p = len(a), len(b), len(b[0])
    result = []
    for i in range(m):
        row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result


# -----------------------------------------------------------------------------
# Menu actions
# -----------------------------------------------------------------------------
def do_transpose():
    rows = read_int("Enter number of rows: ")
    cols = read_int("Enter number of columns: ")
    matrix = read_matrix(rows, cols, "the Matrix")
    display_matrix(matrix, "Original Matrix:")
    display_matrix(transpose_matrix(matrix), "Transposed Matrix:")


def do_addition():
    rows = read_int("Enter number of rows: ")
    cols = read_int("Enter number of columns: ")
    a = read_matrix(rows, cols, "Matrix A")
    b = read_matrix(rows, cols, "Matrix B")
    display_matrix(a, "Matrix A:")
    display_matrix(b, "Matrix B:")
    display_matrix(add_matrices(a, b), "A + B:")


def do_multiplication():
    m = read_int("Enter number of rows for Matrix A (M): ")
    n = read_int("Enter number of columns for Matrix A / rows for Matrix B (N): ")
    p = read_int("Enter number of columns for Matrix B (P): ")
    a = read_matrix(m, n, "Matrix A")
    b = read_matrix(n, p, "Matrix B")
    display_matrix(a, "Matrix A:")
    display_matrix(b, "Matrix B:")
    product = multiply_matrices(a, b)
    if product is None:
        print("Error: columns of A must equal rows of B.")
    else:
        display_matrix(product, "A x B:")


def main():
    actions = {
        "1": do_transpose,
        "2": do_addition,
        "3": do_multiplication,
    }
    while True:
        print("\n=========== MATRIX OPERATIONS ===========")
        print("1. Transpose a matrix")
        print("2. Add two matrices")
        print("3. Multiply two matrices")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "4":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please pick 1, 2, 3 or 4.")
        else:
            action()


if __name__ == "__main__":
    main()