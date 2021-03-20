from random import randint, random


class MinConflictsAlgorithm:
    def __init__(self, csp):
        self.csp = csp
        self.minconflict_vals = self.init_minconflict_vals(csp)

    # initially, all the min_conflict values are -1
    def init_minconflict_vals(self, csp):
        min_conflict_arr = []
        for i in range(0, len(csp.variables)):
            min_conflict_arr.append(-1)
        return min_conflict_arr

    # for each variable in csp, reset its current minimum conflict value
    def reset_minconflict_vals(self, csp):
        for i in range(0, len(csp.variables)):
            self.minconflict_vals[i] = -1

    def minconflictsAlgorithm(self, max_steps, csp):
        for i in range(0, max_steps):
            # Check if csp is complete
            if csp.is_solution(csp.variables):
                return True
            variable = self.pickVariable(csp)
            # if you assigned the minConflict value of each variable, restart from a new random assignment
            if variable is None:
                csp = csp.assign_random_values(csp)
                self.reset_minconflict_vals(csp)
                variable = self.pickVariable(csp)
            value = self.pickValue(variable, csp)
            # Add some randomness helps! (Simulated Annealing)
            # rather than restrictedly choosing good moves, we will sometimes also allow bad moves
            keep_randomness = randint(0, 50)
            if keep_randomness < 35:
                variable.value = value
            else:
                variable.value = randint(0, csp.num_colors)
        return False

        # randomly pick a variable that violates the constraints (if the variable has the same color as any of its
        # neighbors). If all the minconflict values are assigned for each variable, returns none, otherwise returns a
        # variable that violates constrains.
    def pickVariable(self, csp):
        inconsistent_vars = []
        # For every variable in csp, if inconsistent with neighbors, add it to list
        for i in range(0, len(csp.variables)):
            if (not csp.is_consistent(color= csp.variables[i].value, variable=csp.variables[i])) \
                    and (self.minconflict_vals[i] == -1):
                inconsistent_vars.append(csp.variables[i])
        if len(inconsistent_vars) == 0:
            return None
        random_value_index = randint(0, len(inconsistent_vars) - 1)
        return inconsistent_vars[random_value_index]

    # this function is used to sort the values from least constraining to most constraining
    def valSortFunc(self, e):
        return e[1]

    # Find values that minimize the total number of violated constraints (over all variables)
    # if there is only one such value, return that
    # if multiple such values exist, pick one randomly and return that
    def pickValue(self, variable, csp):
        number_of_constrained_variables = []
        for i in range(0, len(variable.domain)):
            current_color = variable.domain[i]
            num_of_const_neighbor = 0
            # For every neighbor of this variable,
            for neighbor in variable.neighbors:
                neighbor_color = neighbor.value
                # If domain color conflicts with this neighbor, increment counter.
                if neighbor_color == current_color:
                    num_of_const_neighbor += 1
            # After checking every neighbor for this color, add it to our list.
            number_of_constrained_variables.append([current_color, num_of_const_neighbor])
        number_of_constrained_variables = sorted(number_of_constrained_variables, key=self.valSortFunc)
        return number_of_constrained_variables[0][0]