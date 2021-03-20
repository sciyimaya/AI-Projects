from random import randint


class Csp:
    def __init__(self, variables, num_variables, num_edges, num_colors):
        self.variables = variables
        self.num_variables = num_variables
        self.num_edges = num_edges
        self.num_colors = num_colors

    # checks if the csp is consistent
    # if the given color is same as any of the variable's neighbor's color, its inconsistent
    # returns true if consistent, false otherwise
    def is_consistent(self, color, variable):
        for i in range(0, len(variable.neighbors)):
            if color == variable.neighbors[i].value:
                return False
        return True

    # checks if each variable in assignment has an assigned value
    # returns true if complete, false otherwise
    def assignment_is_complete(self, variables):
        isComplete = True
        for variable in variables:
            if variable.value == -1:
                return False
        return isComplete

    # assign random values for each variable in csp
    # this will be used in minconflicts algorithm
    def assign_random_values(self, csp):
        domain = csp.variables[0].domain
        for variable in csp.variables:
            random_value_index = randint(0, csp.num_colors - 1)
            variable.value = domain[random_value_index]
        return csp

    # if all the given variable's values are consistent (no neighbor has the same color)
    # return True, return false if incomplete
    def is_solution(self, variables):
        for variable in variables:
            if not self.is_consistent(variable.value, variable):
                return False
        return True