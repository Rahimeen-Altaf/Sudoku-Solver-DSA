# Sudoku Solver

The Sudoku Solver project is an advanced Python application designed to efficiently solve Sudoku puzzles. Sudoku is a number puzzle game played on a 9x9 grid, divided into 3x3 subgrids. The objective is to fill in the grid with digits from 1 to 9, ensuring that each row, column, and subgrid contains every digit exactly once.

## Key Features

1. **Grid Support:**
   - The solver supports various Sudoku grid configurations, including the standard 9x9 grid and variations like 4x4. This allows users to enjoy solving puzzles of different complexities.

2. **User-Driven Input:**
   - Users have the flexibility to choose the percentage of their input. They can contribute to the initial puzzle by providing either 30% or 70% of the filled cells. This personalizes the solving experience and allows users to control the puzzle's difficulty.

3. **Backtracking Algorithm:**
   - The solver employs a powerful backtracking algorithm to dynamically generate solutions for the remaining cells of the puzzle. This ensures a challenging and well-balanced solving process.

4. **Python Implementation:**
   - Developed entirely in Python, the project leverages the language's readability and versatility to create a robust Sudoku-solving solution.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/sudoku-solver.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sudoku-solver
   ```

3. Run the program:

   ```bash
   python sudoku_solver.py
   ```

## Usage

1. Upon running the program, you will be prompted to choose the size of the Sudoku grid (4 or 9) and the percentage of filled cells (30 or 70).
2. The program will display the initial Sudoku puzzle with your provided input.
3. Press Enter to see the solution for the remaining cells.

## Conclusion

The Sudoku Solver project not only serves as a practical implementation of algorithmic techniques but also provides an engaging platform for puzzle enthusiasts. By allowing users to actively contribute to the puzzle and giving them a choice in the level of difficulty, the solver offers a personalized and enjoyable experience, contributing to the broader landscape of Python-based algorithmic applications.
