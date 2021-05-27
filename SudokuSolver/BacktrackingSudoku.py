class BacktrackingSudoku:
    def __init__(self, sudoku_problem):
        self.sudoku_problem = sudoku_problem
        self.start_state = sudoku_problem.start_state
        self.solution = []

    def solve_sudoku_backtracking(self, current_state):
        current_cell = [0, 0]
        # if there are no empty cells, success
        if not self.get_unassigned_cell(current_state, current_cell):
            self.solution = current_state
            return True
        row, col = current_cell[0], current_cell[1]
        for i in range(1, 10):
            if self.sudoku_problem.move_is_allowed(current_state, row, col, i):
                current_state[row][col] = i  # apply move
                if self.solve_sudoku_backtracking(current_state):
                    return True
                current_state[row][col] = 0  # unapply move and try again
        return False  # backtrack

    # Searches for an unassigned position at the current State.
    # If found, current_cell is set to be the found position and true is returned.
    # If there are no unassigned positions in the current state, false is returned
    def get_unassigned_cell(self, current_state, current_cell):
        for r in range(0, 9):
            for c in range(0, 9):
                if current_state[r][c] == 0:
                    current_cell[0] = r
                    current_cell[1] = c
                    return True
        return False

    # Stringify the solution
    def getSolution(self):
        output = ''
        for row in self.solution:
            strippedRow = ''
            for cell in row:
                if cell != 0:
                    strippedRow += str(cell)
                else:
                    return False
                strippedRow += ' '
            output += strippedRow
            output += '\n'
        return output
