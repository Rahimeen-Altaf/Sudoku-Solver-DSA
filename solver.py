import os

CLEAR = 'cls'  # Assuming you're using Windows, change to 'clear' if you're on Linux or MacOS

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

user_input_size = get_user_input_size()
user_input_percentage = get_user_input_percentage()

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

sudoku = []
row = []

for i in range(len(puzzle)):
    row.append(int(puzzle[i]))
    if (i + 1) % user_input_size == 0:
        sudoku.append(row)
        row = []

def solve(board):
    find = is_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, user_input_size + 1):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            os.system(CLEAR)
            print("\nSolution: \n")
            print_sudoku(sudoku)

            if solve(board):
                return True

            board[row][col] = 0

    return False

def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

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

os.system(CLEAR)
print("\nProblem: \n")
print_sudoku(sudoku)

input("\nPress Enter to See the Solution...")
solve(sudoku)

my_solution = ''
for i in range(user_input_size):
    for j in range(user_input_size):
        my_solution = my_solution + str(sudoku[i][j])

if my_solution == solution:
    os.system(CLEAR)
    print("\nThe solution is verified\n")
    print_sudoku(sudoku)
else:
    os.system(CLEAR)
    print("\nExpected Solution: \t", solution)
    print("Your Solution: \t\t", my_solution)
    print("\nYour solution is incorrect. Please try again.")