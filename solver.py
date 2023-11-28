import os
import random

CLEAR = 'cls'

from puzzles import puzzle70_0 as puzzle_70
from puzzles import puzzle30_0 as puzzle_30

from solutions import solution70_0 as solution_70
from solutions import solution30_0 as solution_30

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


user_input_percentage = get_user_input_percentage()
if user_input_percentage == 30:
    puzzle = puzzle_30
    solution = solution_30
else:
    puzzle = puzzle_70
    solution = solution_70

sudoku = []
row = []

for i in range(len(puzzle)):
    row.append(int(puzzle[i]))
    if (i+1) % 9 == 0:
        sudoku.append(row)
        row = []

def solve(board):
    find = is_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            os.system(CLEAR)        #Comment this line if you don't want to see the solution to increase the speed
            print("\nSolution: \n") #Comment this line if you don't want to see the solution to increase the speed
            print_sudoku(sudoku)    #Comment this line if you don't want to see the solution to increase the speed

            if solve(board):
                return True

            board[row][col] = 0

    return False

def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    boardx_x = pos[1] // 3
    boardx_y = pos[0] // 3

    for i in range(boardx_y*3, boardx_y*3 + 3):
        for j in range(boardx_x * 3, boardx_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------+-------+-------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                if board[i][j] == 0:
                    print(" ")
                else:
                    print(board[i][j])
            else:
                if board[i][j] == 0:
                    print(" " + " ", end="")
                else:
                    print(str(board[i][j]) + " ", end="")

def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

os.system(CLEAR)
print("\nProblem: \n")
print_sudoku(sudoku) # Unsolved

input("\nPress Enter to See the Solution...")
solve(sudoku)


os.system(CLEAR)
print("\nProblem: \n")
print_sudoku(sudoku)  # Unsolved

input("\nPress Enter to See the Solution...")
solve(sudoku)

mySolution = ''
for i in range(9):
    for j in range(9):
        mySolution = mySolution + str(sudoku[i][j])

if mySolution == solution:
    os.system(CLEAR)
    print("\nThe solution is verified\n")
    print_sudoku(sudoku)
else:
    os.system(CLEAR)
    print("\nExpected Solution: \t", solution)
    print("Your Solution: \t\t", mySolution)
    print("\nYour solution is incorrect. Please try again.")