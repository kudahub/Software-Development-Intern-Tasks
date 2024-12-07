def print_grid(grid):
    """Print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))
    print()


def is_valid(grid, row, col, num):
    """
    Check if placing a number at grid[row][col] is valid.
    """
    # Check the row
    if num in grid[row]:
        return False

    # Check the column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):
    """
    Solve the Sudoku puzzle using backtracking.
    """
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Empty cell found
                for num in range(1, 10):  # Try numbers 1 through 9
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num  # Place the number

                        if solve_sudoku(grid):  # Recurse
                            return True

                        grid[row][col] = 0  # Backtrack
                return False
    return True


def sudoku_solver():
    """
    Main function to input and solve Sudoku.
    """
    print("Enter the Sudoku grid (row by row, use 0 for empty cells):")
    grid = []

    for i in range(9):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != 9:
            print("Each row must contain exactly 9 numbers.")
            return
        grid.append(row)

    print("\nUnsolved Sudoku Grid:")
    print_grid(grid)

    if solve_sudoku(grid):
        print("Solved Sudoku Grid:")
        print_grid(grid)
    else:
        print("No solution exists for the given Sudoku puzzle.")


# Run the program
sudoku_solver()
