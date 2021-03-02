import copy

# this class defines the search problem
class TileProblem:
    def __init__(self, start_state, puzzle_size):
        self.start_state = start_state
        self.puzzle_size = puzzle_size  # n = 3 for 8-puzzle or n = 4 for 15-puzzle
        if puzzle_size == 3:
            self.goal_state = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
        else:
            self.goal_state = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '0']
        self.actions = ['U', 'D', 'L', 'R']

    # apply the action to the current_state and return the resulting state
    def transition_function(self, action, current_state):
        new_state = copy.deepcopy(current_state)
        # 8-puzzle problem
        if self.puzzle_size == 3:
            if action == 'U':
                old_blank_index = current_state.index('0')
                new_blank_index = old_blank_index - 3
                new_state[old_blank_index] = current_state[new_blank_index]
                new_state[new_blank_index] = '0'
                return new_state
            elif action == 'D':
                old_blank_index = current_state.index('0')
                new_blank_index = old_blank_index + 3
                new_state[old_blank_index] = current_state[new_blank_index]
                new_state[new_blank_index] = '0'
                return new_state
            elif action == 'R':
                old_blank_index = current_state.index('0')
                new_blank_index = old_blank_index + 1
                new_state[old_blank_index] = current_state[new_blank_index]
                new_state[new_blank_index] = '0'
                return new_state
            else:  # action == 'L'
                old_blank_index = current_state.index('0')
                new_blank_index = old_blank_index - 1
                new_state[old_blank_index] = current_state[new_blank_index]
                new_state[new_blank_index] = '0'
                return new_state

        # 15-puzzle problem
        elif self.puzzle_size == 4:
            if action == 'U':
                old_blank_index = current_state.index('0')
                new_blank_index = old_blank_index - 4
                new_state[old_blank_index] = current_state[new_blank_index]
                new_state[new_blank_index] = '0'
                return new_state
            elif action == 'D':
                old_blank_index = current_state.index('0')
                new_blank_index = old_blank_index + 4
                new_state[old_blank_index] = current_state[new_blank_index]
                new_state[new_blank_index] = '0'
                return new_state
            elif action == 'R':
                old_blank_index = current_state.index('0')
                new_blank_index = old_blank_index + 1
                new_state[old_blank_index] = current_state[new_blank_index]
                new_state[new_blank_index] = '0'
                return new_state
            else:  # action == 'L'
                old_blank_index = current_state.index('0')
                new_blank_index = old_blank_index - 1
                new_state[old_blank_index] = current_state[new_blank_index]
                new_state[new_blank_index] = '0'
                return new_state

    # check if the provided state is the goal state
    def goal_test(self, current_state):
        if current_state == self.goal_state:
            return True
        else:
            return False
