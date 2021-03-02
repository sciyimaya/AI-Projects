from Heuristics import Heuristics
from stateNode import stateNode


class Rbfs_Algorithm:
    def __init__(self, tile_problem, heuristics):
        self.heuristics = heuristics
        self.tile_problem = tile_problem
        self.start_state = tile_problem.start_state
        self.failure = stateNode(['F'], None, -1, 'F', 3)

    # implementation of rbfs algorithm
    def rbfs(self, current_node, f_limit):
        if self.tile_problem.goal_test(current_node.state):
            return current_node, 0  # success
        successors = []
        # add children of current_node to successors
        for action in current_node.possible_actions:
            new_state = self.tile_problem.transition_function(action, current_node.state)
            new_node = self.make_node(new_state, current_node, action)
            successors.append(new_node)
        successors.sort(key=lambda stateNode: stateNode.f_val)  # sort by f_val
        if len(successors) == 0:
            return self.failure, float('inf')
        for s in successors:
            s.f_val = max(current_node.f_val, self.compute_fval(s.state, current_node.g_val))

        while True:
            successors.sort(key=lambda stateNode: stateNode.f_val)  # sort by f_val
            best_node = successors[0]
            if best_node.f_val > f_limit:
                return self.failure, best_node.f_val
            alternative = successors[1].f_val
            result, best_node.f_val = self.rbfs(best_node, min(f_limit, alternative))
            if result.f_val != self.failure.f_val:
                return result, 0

    def myFunc(e):
        return e['f_val']

    # constructs and returns a new node given the state of the node to be constructed, parent, and action
    def make_node(self, new_state, parent, action):
        puzzle_size = self.tile_problem.puzzle_size
        if parent is None:
            f_val = self.compute_fval(new_state, -1)
        else:
            f_val = self.compute_fval(new_state, parent.g_val)
        newNode = stateNode(new_state, parent, f_val, action, puzzle_size)
        return newNode

    # this method calculates the f value given the state
    # and parent's gval by calling a heuristic function
    def compute_fval(self, state, parent_gval):
        h_class = Heuristics()
        if self.heuristics == 1:
            h_val = h_class.h1(state, self.tile_problem.goal_state)
        else:
            h_val = h_class.h2(state, self.tile_problem.goal_state)
        return h_val + parent_gval + 1