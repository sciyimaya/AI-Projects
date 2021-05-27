"""
    This class defines the sudoku problem
"""

class SudokuProblem:
    def __init__(self, start_state):
        self.start_state = start_state

    # if no number given at row and column does not match the given number
    # and if the given number is not already assigned to a position at its
    # same 3x3 subgrid return true, otherwise return false
    def move_is_allowed(self, current_state, row, col, num):
        # check if the given number is assigned to a position at the given row or column
        for i in range(0, 9):
            if (current_state[row][i] == num) or (current_state[i][col] == num):
                return False

        # check if any cell within the given position's 3x3 subgrid matches the given number
        subgrid_row = row - row % 3
        subgrid_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if current_state[i + subgrid_row][j + subgrid_col] == num:
                    return False
        return True

    # check if the provided state is a goal state
    def goal_test(self, current_state):
        for r in range(0, 9):
            for c in range(0, 9):
                if not self.move_is_allowed(current_state, r, c, current_state[r][c]):
                    return False
        return True