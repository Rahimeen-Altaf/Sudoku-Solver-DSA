import os
import platform

# Clear the console screen based on the operating system
if platform.system() == 'Windows':
    CLEAR = 'cls'
else:
    CLEAR = 'clear'

# Function to get user input for the size of the Sudoku grid
def get_user_input_size():
    while True:
        try:
            size = int(input("Enter the size of the Sudoku grid (4 or 9): "))
            if size == 4 or size == 9:
                return size
            else:
                print("Invalid input. Please enter 4 or 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get user input for the percentage of input in the puzzle
def get_user_input_percentage():
    while True:
        try:
            percentage = int(input("Enter the percentage of input you want (30 or 70): "))
            if percentage == 30 or percentage == 70:
                return percentage
            else:
                print("Invalid input. Please enter 30 or 70.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get user inputs for grid size and percentage of input
user_input_size = get_user_input_size()
user_input_percentage = get_user_input_percentage()

# Load puzzle and solution based on user input
if user_input_size == 4:
    if user_input_percentage == 30:
        from puzzles import puzzle4x4_30_0 as puzzle
        from solutions import solution4x4_30_0 as solution
    else:
        from puzzles import puzzle4x4_70_0 as puzzle
        from solutions import solution4x4_70_0 as solution
elif user_input_size == 9:
    if user_input_percentage == 30:
        from puzzles import puzzle9x9_30_0 as puzzle
        from solutions import solution9x9_30_0 as solution
    else:
        from puzzles import puzzle9x9_70_0 as puzzle
        from solutions import solution9x9_70_0 as solution

# Initialize the Sudoku grid
sudoku = []
row = []

# Convert puzzle string to a 2D list
for i in range(len(puzzle)):
    row.append(int(puzzle[i]))
    if (i + 1) % user_input_size == 0:
        sudoku.append(row)
        row = []

# Function to solve the Sudoku puzzle using backtracking
def solve(board):
    # Find an empty cell in the Sudoku grid
    find = is_empty(board)
    
    # If no empty cell is found, the puzzle is solved
    if not find:
        return True
    else:
        row, col = find

    # Try placing numbers from 1 to the grid size in the empty cell
    for i in range(1, user_input_size + 1):
        # Check if placing the current number is valid in the current position
        if is_valid(board, i, (row, col)):
            # Place the number in the cell
            board[row][col] = i
            os.system(CLEAR)
            print("\nSolution: \n")
            print_sudoku(sudoku)

            # Recursively attempt to solve the rest of the puzzle
            if solve(board):
                return True

            # If placing the current number doesn't lead to a solution, backtrack by resetting the cell to 0
            board[row][col] = 0

    # If no number can be placed in the current cell, backtrack to the previous cell
    return False


# Function to find an empty cell in the Sudoku grid
def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

# Function to check if a number can be placed in a specific position
def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    boardx_x = pos[1] // int(user_input_size**0.5)
    boardx_y = pos[0] // int(user_input_size**0.5)

    for i in range(boardx_y * int(user_input_size**0.5), boardx_y * int(user_input_size**0.5) + int(user_input_size**0.5)):
        for j in range(boardx_x * int(user_input_size**0.5), boardx_x * int(user_input_size**0.5) + int(user_input_size**0.5)):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

# Function to print the Sudoku grid
def print_sudoku(board):
    for i in range(len(board)):
        if i % int(user_input_size**0.5) == 0 and i != 0:
            print("-" * (user_input_size*2 + int(user_input_size**0.5)))

        for j in range(len(board[0])):
            if j % int(user_input_size**0.5) == 0 and j != 0:
                print("| ", end="")

            if j == user_input_size - 1:
                if board[i][j] == 0:
                    print(" ")
                else:
                    print(board[i][j])
            else:
                if board[i][j] == 0:
                    print(" " + " ", end="")
                else:
                    print(str(board[i][j]) + " ", end="")

# Display the initial problem
os.system(CLEAR)
print("\nProblem: \n")
print_sudoku(sudoku)

# Wait for user input before displaying the solution
input("\nPress Enter to See the Solution...")

# Solve the Sudoku puzzle
solve(sudoku)

# Convert the solution to a string for verification
my_solution = ''
for i in range(user_input_size):
    for j in range(user_input_size):
        my_solution = my_solution + str(sudoku[i][j])

# Verify the solution
if my_solution == solution:
    os.system(CLEAR)
    print("\nThe solution is verified\n")
    print_sudoku(sudoku)
else:
    os.system(CLEAR)
    print("\nExpected Solution: \t", solution)
    print("Your Solution: \t\t", my_solution)
    print("\nYour solution is incorrect. Please try again.")
