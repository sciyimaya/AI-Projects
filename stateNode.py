import copy

# this class defines a node object which has a state, parent, f_val, g_val,
# actions that applied till current state, puzzle_size, and possible actions from this state
class stateNode:
    def __init__(self, state, parent, f_val, new_action, puzzle_size):
        if state[0] == 'F':
            self.f_val = -1
        else:
            self.parent = parent
            if parent is None:
                self.g_val = 0
                self.actions_till_now = list()
            else:
                self.g_val = parent.g_val + 1
                self.actions_till_now = copy.deepcopy(parent.actions_till_now)
                self.actions_till_now.append(new_action)
            self.state = state
            self.puzzle_size = puzzle_size
            self.possible_actions = self.determine_actions(state)
            self.f_val = f_val

    # given a state, return a list of possible actions
    def determine_actions(self, state):
        actions = []
        # 8-puzzle problem
        if self.puzzle_size == 3:
            # if blank tile is not in indices 0, 1, or 2, 'U' is possible
            if (state[0] != '0') and (state[1] != '0') and (state[2] != '0'):
                actions.append('U')
            # if blank tile is not in indices 6, 7, or 8, 'D' is possible
            if state[6] != '0' and state[7] != '0' and state[8] != '0':
                actions.append('D')

            # if blank tile is not in indices 2, 5, or 8, 'R' is possible
            if state[2] != '0' and state[5] != '0' and state[8] != '0':
                actions.append('R')

            # if blank tile is not in indices 0, 3, or 6, 'L' is possible
            if state[0] != '0' and state[3] != '0' and state[6] != '0':
                actions.append('L')

        # 15-puzzle problem
        elif self.puzzle_size == 4:
            # if blank tile is not in indices 0, 1, 2, or 3, 'U' is possible
            if (state[0] != '0') and (state[1] != '0') and (state[2] != '0') and (state[3] != '0'):
                actions.append('U')
            # if blank tile is not in indices 12, 13, 14, or 15 'D' is possible
            if (state[12] != '0') and (state[13] != '0') and (state[14] != '0') and (state[15] != '0'):
                actions.append('D')

            # if blank tile is not in indices 3, 7, 11, 15, 'R' is possible
            if (state[3] != '0') and (state[7] != '0') and (state[11] != '0') and (state[15] != '0'):
                actions.append('R')

            # if blank tile is not in indices 0, 4, 8, 12, 'L' is possible
            if (state[0] != '0') and (state[4] != '0') and (state[8] != '0') and (state[12] != '0'):
                actions.append('L')
        return actions
