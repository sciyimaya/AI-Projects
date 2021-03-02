from Heuristics import Heuristics
from Priority_Queue import Priority_Queue
from stateNode import stateNode


class A_star_Algorithm:
    def __init__(self, tile_problem, heuristics):
        self.heuristics = heuristics
        self.tile_problem = tile_problem
        self.start_state = tile_problem.start_state
        self.frontier = Priority_Queue()
        self.explored = []

    # this method implements the a* algorithm
    def a_star(self):
        self.frontier.insert(self.make_node(self.tile_problem.start_state, None, None)) # make a node from start state, and add it to frontier
        while len(self.frontier.my_queue) != 0:
            current_node = self.frontier.pop()
            if self.tile_problem.goal_test(current_node.state):
                return current_node.actions_till_now    # success
            if not self.explored.__contains__(current_node.state):
                self.explored.append(current_node.state)    #if not already explored, add current state to explored
                # for each action that is possible from the current state do:
                for action in current_node.possible_actions:
                    new_state = self.tile_problem.transition_function(action, current_node.state) # apply the action to new state to get a new state
                    new_node = self.make_node(new_state, current_node, action)  # make the new state a new node
                    self.frontier.insert(new_node)  # add the new node to frontier
        return []   # if a solution is not found, return empty list

    # constructs and returns a new node given the state of the node to be constructed, parent, and action
    def make_node(self, new_state, parent, action):
        puzzle_size = self.tile_problem.puzzle_size
        if parent is None:
            f_val = self.compute_fval(new_state, -1)    # if it's the start state, f_val should be equal to h_val
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
