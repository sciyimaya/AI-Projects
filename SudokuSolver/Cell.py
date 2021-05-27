import copy

class Cell:
    def __init__(self, assignment):
        self.assignment = assignment
        self.candidates = []

    def determine_candidates(self, row, col, current_state, sudoku_problem):
        candidates = []
        new_state = copy.deepcopy(current_state)
        if current_state[0][0] is Cell:
            # convert grid into normal 2D array with assignments only
            for r in range(0, 9):
                for c in range(0, 9):
                    new_state[r][c] = current_state[r][c].assignment

        for i in range(1, 10):
            if sudoku_problem.move_is_allowed(current_state, row, col, i):
                candidates.append(i)
        return candidates
