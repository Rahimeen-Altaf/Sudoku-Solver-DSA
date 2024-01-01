import os
import platform

# Clear the console screen based on the operating system
if platform.system() == 'Windows':
    CLEAR = 'cls'
else:
    CLEAR = 'clear'

# Function to load puzzle data from a text file
def load_puzzle_data(size, percentage):
    filename = 'puzzles.txt'
    with open(filename, 'r') as file:
        content = file.read()
        puzzles = content.split('\n\n')  # Each puzzle is separated by two newline characters

    target_label = f'{size}x{size} {percentage}% puzzles'
    for puzzle_section in puzzles:
        if target_label in puzzle_section:
            puzzle_lines = puzzle_section.split('\n')
            puzzle = ''.join(puzzle_lines[1])
            return puzzle

    print(f"No puzzle found for size {size} and percentage {percentage}.")
    return ""  # or return a default puzzle or handle the situation accordingly



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

# Load puzzle based on user input
puzzle = load_puzzle_data(user_input_size, user_input_percentage)

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

def solution_checker(board):
    ''' solution checker replacing solution.py by utilizing the is_valid function to check the final grid if it is up to the mark.'''
    for i in range(len(board)):
        for j in range(len(board[0])):
            num = board[i][j]

            # Check row, column, and subgrid constraints
            if not is_valid(board, num, (i, j)):
                print(f"Constraint violated at ({i}, {j}): {num}")
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

if solution_checker(sudoku):
    os.system(CLEAR)
    print_sudoku(sudoku)
    print("\nThe solution is verified\n")
else:
    os.system(CLEAR)
    print("\nYour solution is incorrect. Please try again.")
