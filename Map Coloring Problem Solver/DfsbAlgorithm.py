import copy
import time
from MyQueue import MyQueue


class DfsbAlgorithm:
    def __init__(self, csp):
        self.csp = csp
        self.queue = MyQueue()
        self.depth = 0


    # This method has the implementation of simple recursive backtracking
    # csp: contains the variables and the constraints we have
    # @returns success or failure
    # - check if the assignment is complete, if yes return success
    # - select an unassigned variable
    # - for each color in the selected variable's domain, check if its consistent
    #   - if the color is consistent, assign it and recursively call DFSB plain
    #   - once DFSB plain returns, if we have success, return success, otherwise remove the assigned value
    def dfsb_plain(self, csp):
        if csp.assignment_is_complete(csp.variables):
            return True
        variable = self.select_unassigned_variable(csp.variables)
        for current_color in variable.domain:
            if csp.is_consistent(color=current_color, variable=variable):
                variable.value = current_color
                result = self.dfsb_plain(csp)
                if result is not None:
                    return result
                variable.value = -1
        return None

    # selects an unassigned variable and returns it
    # @returns the unassigned variable, None if none exists
    def select_unassigned_variable(self, variables):
        for variable in variables:
            if variable.value == -1:
                return variable
        return None

    # this method has the implementation of improved recursive backtracking
    # assignment: an array of colors where each index i represents var_i's color.
    # if no color is assigned for var_i, assignment[i] is -1
    # csp: contains the variables and the constraints we have
    # @returns solution or failure
    def dfsb_improved(self, csp):
        if csp.assignment_is_complete(csp.variables):
            return True
        variable = self.select_most_constrained_variable(csp.variables)
        self.order_domain_values(variable, csp)
        for current_color in variable.domain:
            if csp.is_consistent(color=current_color, variable=variable):
                variable.value = current_color
                variable.domain = [current_color]
                self.initialize_queue(csp)
                self.ac_3(csp)
                result = self.dfsb_improved(csp)
                if result:
                    return True
                variable.value = -1
                self.resetDomains(csp)
        return False

    # this method resets the domain of unassigned variables by setting them e.g. [0, 1, 2] for K = 3
    def resetDomains(self, csp):
        for variable in csp.variables:
            if variable.value == -1:
                variable.domain = []
                for i in range(0, csp.num_colors):
                    variable.domain.append(i)

    # add all the arcs: if A and B are adjacent, A->B and B->A are arcs
    # tail of the arcs is unassigned
    def initialize_queue(self, csp):
        for variable in csp.variables:
            if variable.value == -1:
                for neighbor in variable.neighbors:
                    self.queue.enqueue([variable, neighbor])

    # This method implements the Arc Consistency algorithm
    # prunes the current set of possibilities
    def ac_3(self, csp):
        while not self.queue.isEmpty():
            [tail, head] = self.queue.dequeue()  # pop one arc at a time
            if self.remove_inconsistent_values(tail, head):  # if the arc is inconsistent, make it consistent then:
                for neighbor in tail.neighbors:
                    if (not self.queue.contains([neighbor, tail])) & (neighbor.value == -1):
                        self.queue.enqueue([neighbor, tail])  # add all the neighbors of tail to queue for pruning

    # makes the arc consistent by removing the values from tail that are making it inconsistent
    # returns true if anything is removed, false otherwise
    def remove_inconsistent_values(self, tail, head):
        removed = False
        found_different_value = 0

        # if head has a value
        if head.value != -1:
            for tail_color in tail.domain:
                if tail_color == head.value:
                    tail.domain.remove(tail_color)
                    removed = True

        elif head.value == -1:
            for tail_color in tail.domain:
                for head_color in head.domain:
                    if tail_color != head_color:
                        found_different_value = 1
                if found_different_value != 1:
                    tail.domain.remove(tail_color)
                    removed = True
                found_different_value = 0
        return removed

    # to sort the variables based on their domain size
    def numValsFunc(self, e):
        return len(e.domain)

    # select the most constrained variable (the variable with the least number of values in its domain)
    # @returns the most constrained variable
    def select_most_constrained_variable(self, variables):
        most_constrained_vars = []
        for i in range(0, len(variables)):
            if variables[i].value == -1:
                most_constrained_vars.append(variables[i])

        # sort the values from most constrained to least constrained
        most_constrained_vars.sort(key=self.numValsFunc)
        return most_constrained_vars[0]

    # sorts the values based on the number of constraints they cause
    def valSortFunc(self, e):
        return e[1]

    # order the domain of the given variable from least constraining value to most constraining value
    # assume the value for the variable and use the constraint graph to
    # check how many values remain for the other variables
    def order_domain_values(self, variable, csp):
        num_val_remaining = []
        for i in range(0, len(variable.domain)):
            current_color = variable.domain[i]
            num_val_remaining.append([current_color, 0])
            for neighbor in variable.neighbors:
                if csp.is_consistent(color=current_color, variable=variable):
                    if neighbor.domain.count(current_color) > 0:  # if the chosen color is in neighbor's add 1 to number of constraints
                        num_val_remaining[i][1] += 1
                else:  # if the color is inconsistent, add it to end
                    num_val_remaining[i][1] = csp.num_edges

        # sort the list from least constraining value to most constraining value
        num_val_remaining = sorted(num_val_remaining, key=self.valSortFunc)
        for i in range(0, len(variable.domain)):
            variable.domain[i] = num_val_remaining[i][0]