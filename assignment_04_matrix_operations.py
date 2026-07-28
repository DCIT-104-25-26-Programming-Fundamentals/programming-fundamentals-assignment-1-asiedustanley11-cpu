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

def read_matrix(rows, cols, label=""):
    """
    Prompt the user to enter a matrix of the given size, one row at a
    time (values separated by spaces), and return it as a list of lists.
    """
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}{label}: ")
            values = row_input.split()
 
            # Make sure the row has exactly the right number of values
            if len(values) != cols:
                print(f"Please enter exactly {cols} numbers.")
                continue
 
            try:
                row = [float(v) for v in values]
            except ValueError:
                print("Please enter valid numbers separated by spaces.")
                continue
 
            matrix.append(row)
            break
 
    return matrix
 
 
def display_matrix(matrix, title="Matrix"):
    """
    Print a matrix in a neat, aligned grid format.
    """
    print(f"\n{title}:")
    for row in matrix:
        # Format each number, stripping trailing ".0" for whole numbers
        formatted_row = []
        for value in row:
            if value == int(value):
                formatted_row.append(f"{int(value):6d}")
            else:
                formatted_row.append(f"{value:6.2f}")
        print(" ".join(formatted_row))
 
 
# -----------------------------------------------------------------------------
# PART A — Transpose
# -----------------------------------------------------------------------------
def transpose_matrix(matrix):
    """
    Return the transpose of the given matrix (rows become columns).
    """
    rows = len(matrix)
    cols = len(matrix[0])
 
    # Build an empty result matrix of size cols x rows
    result = [[0 for _ in range(rows)] for _ in range(cols)]
 
    # Nested loop: for every position (i, j) in the original,
    # place the value at position (j, i) in the result.
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
 
    return result
 
 
# -----------------------------------------------------------------------------
# PART B — Addition
# -----------------------------------------------------------------------------
def add_matrices(matrix_a, matrix_b):
    """
    Return the element-wise sum of two matrices of the same size.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
 
    result = [[0 for _ in range(cols)] for _ in range(rows)]
 
    # Nested loop: add the matching elements from both matrices.
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
 
    return result
 
 
# -----------------------------------------------------------------------------
# PART C — Multiplication
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b):
    """
    Return the matrix product of matrix_a (M x N) and matrix_b (N x P).
    The result is an M x P matrix.
    """
    m = len(matrix_a)          # rows in A
    n = len(matrix_a[0])       # columns in A (must equal rows in B)
    p = len(matrix_b[0])       # columns in B
 
    result = [[0 for _ in range(p)] for _ in range(m)]
 
    # Triple nested loop:
    #   i -> each row of A
    #   j -> each column of B
    #   k -> walks along the shared dimension (columns of A / rows of B),
    #        multiplying and summing to get one entry of the result.
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total
 
    return result
 
 
def get_positive_int(prompt):
    """
    Ask the user for a positive whole number, re-prompting until valid.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive whole number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")
 
 
def main():
    print("=== MATRIX OPERATIONS ===")
 
    # -------------------------------------------------------------------
    # PART A — Transpose
    # -------------------------------------------------------------------
    print("\n--- Part A: Transpose a Matrix ---")
    rows = get_positive_int("Enter number of rows: ")
    cols = get_positive_int("Enter number of columns: ")
    matrix = read_matrix(rows, cols)
 
    display_matrix(matrix, "Original Matrix")
    transposed = transpose_matrix(matrix)
    display_matrix(transposed, "Transposed Matrix")
 
    # -------------------------------------------------------------------
    # PART B — Addition
    # -------------------------------------------------------------------
    print("\n--- Part B: Add Two Matrices ---")
    rows_b = get_positive_int("Enter number of rows for both matrices: ")
    cols_b = get_positive_int("Enter number of columns for both matrices: ")
 
    print("Matrix A:")
    matrix_a = read_matrix(rows_b, cols_b)
    print("Matrix B:")
    matrix_b = read_matrix(rows_b, cols_b)
 
    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    sum_matrix = add_matrices(matrix_a, matrix_b)
    display_matrix(sum_matrix, "Sum (A + B)")
 
    # -------------------------------------------------------------------
    # PART C — Multiplication
    # -------------------------------------------------------------------
    print("\n--- Part C: Multiply Two Matrices ---")
    m = get_positive_int("Enter rows for Matrix A: ")
    n = get_positive_int("Enter columns for Matrix A (= rows for Matrix B): ")
    p = get_positive_int("Enter columns for Matrix B: ")
 
    print("Matrix A:")
    matrix_c = read_matrix(m, n)
    print("Matrix B:")
    matrix_d = read_matrix(n, p)
 
    display_matrix(matrix_c, "Matrix A")
    display_matrix(matrix_d, "Matrix B")
    product_matrix = multiply_matrices(matrix_c, matrix_d)
    display_matrix(product_matrix, "Product (A x B)")
 
 
if __name__ == "__main__":
    main() 
