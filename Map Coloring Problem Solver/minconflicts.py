import sys
import datetime
from random import randint

from Csp import Csp
from MinConflictsAlgorithm import MinConflictsAlgorithm
from VariableNode import VariableNode


# if no solution is found within a reasonable time(60 sec) then write No Answer to the provided output file
def write_failure(output_file):
    output_file.write("No Answer")


# writes the solution to the provided output file
def write_output(output_file, csp):
    for i in range(len(csp.variables)):
        output_file.write(str(csp.variables[i].value))
        if i != (len(csp.variables) - 1):
            output_file.write('\n')


# this method creates a variable_node for each variable
# @returns an array of variable nodes
def initialize_variables(num_variables, num_colors):
    variables = []
    for i in range(0, num_variables):
        variables.append(VariableNode(i, num_colors))
    return variables


# this method constructs a csp object given the input file
# @returns the constructed csp object
def construct_csp(in_file):
    lines = in_file.readlines()

    n_m_k = lines[0].split()
    num_variables = int(n_m_k[0])
    num_edges = int(n_m_k[1])
    num_colors = int(n_m_k[2].strip())
    variables = initialize_variables(num_variables, num_colors)

    # add neighbors to each variable
    for i in range(1, num_edges + 1):
        adjacent_variables = lines[i].split()
        varA_name = int(adjacent_variables[0])
        varB_name = int(adjacent_variables[1].strip())
        varA = variables[varA_name]
        varB = variables[varB_name]
        varA.add_neighbor(varB)
        varB.add_neighbor(varA)

    return Csp(variables, num_variables, num_edges, num_colors)

if __name__ == '__main__':
    input_file = ''
    out_file = ''

    input_file = open(sys.argv[1], 'r')
    out_file = open(sys.argv[2], 'w')

    # get the initial state from input file
    csp = construct_csp(input_file)

    solution = []
    minConflicts = MinConflictsAlgorithm(csp)

    max_steps = csp.num_colors ** csp.num_variables # max steps is the depth
    csp = csp.assign_random_values(csp)
    could_solve = minConflicts.minconflictsAlgorithm(max_steps, csp)
    if could_solve:
        write_output(out_file, csp)
    else:
        write_failure(out_file)

    input_file.close()
    out_file.close()
