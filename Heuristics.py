class Heuristics:
    # number of misplaced tiles
    def h1(self, current_state, goal_state):
        counter = 0
        for i in range(0, len(current_state)):
            if i == (len(current_state) - 1):
                if current_state[i] != '0':
                    counter += 1
            else:
                if current_state[i] != goal_state[i]:
                    counter += 1
        return counter

    # number of misplaced tiles, disregarding the last 4 places
    def h2(self, current_state, goal_state):
        counter = 0
        for i in range(0, len(current_state) - 4):
            if current_state[i] != goal_state[i]:
                counter += 1
        return counter

