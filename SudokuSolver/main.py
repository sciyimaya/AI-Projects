from BacktrackingSudoku import BacktrackingSudoku
from SudokuProblem import SudokuProblem
from Sudoku import Sudoku
from RuleBasedSudoku import RuleBasedSudoku
import json
import sys

if __name__ == '__main__':
    # get the inputs
    algorithm = int(sys.argv[1])

    # Get the problems
    sudokuProblems = list()
    with open('generatedSudokus', 'r') as f:
        readLine = f.readline()
        while readLine != '':
            problem = json.loads(readLine)
            sudokuProblems.append(problem)
            readLine = f.readline()

    if algorithm == 1:  # Backtracking
        sudoku_problem = SudokuProblem(sudokuProblems[0])
        backtracking = BacktrackingSudoku(sudoku_problem)
        couldSolve = backtracking.solve_sudoku_backtracking(sudokuProblems[0])
        print(backtracking.getSolution()) if backtracking.getSolution() else print('No solution')

    elif algorithm == 2:  # Rule Based
        sudokuProblem = Sudoku(sudokuProblems[0])
        ruleBased = RuleBasedSudoku()
        solution = ruleBased.solveProblem(sudokuProblem)
        print(solution.getSolution()) if solution else print('No Solution')

    elif algorithm == 3:  # Boltzmann Machine
        print("Boltzmann Machine")

    else:
        print("Please enter a valid algorithm. Options: 1 (Backtracking), 2 (Boltzmann Machine), 3 (Rule Based)")

