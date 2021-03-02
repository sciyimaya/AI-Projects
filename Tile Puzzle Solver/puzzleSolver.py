import sys
import datetime

from A_star_Algorithm import A_star_Algorithm
from Rbfs_Algorithm import Rbfs_Algorithm
from TileProblem import TileProblem

# this method constructs an array of tiles from the given file
# @returns start_state: an array containing the initial state of the board
def construct_start_state(in_file):
    start_state = []
    lines = in_file.readlines()
    for line in lines:
        start_state = start_state + line.split(',')
    for input_str in start_state:
        if input_str.endswith('\n'):
            start_state[start_state.index(input_str)] = input_str[0:input_str.__len__() - 1]
            if start_state[start_state.index(input_str[0:input_str.__len__() - 1])] == '':
                start_state[start_state.index(input_str[0:input_str.__len__() - 1])] = '0'
        if input_str == '':
            start_state[start_state.index(input_str)] = '0'
    return start_state


# writes the solution to the provided output file
def write_output(output_file, solution):
    for i in range(len(solution)):
        output_file.write(solution[i])
        if i != (len(solution) - 1):
            output_file.write(",")


if __name__ == '__main__':
    input_file = ''
    out_file = ''

    algorithm = int(sys.argv[1])
    puzzle_size = int(sys.argv[2])
    heuristics = int(sys.argv[3])
    input_file = open(sys.argv[4], 'r')
    out_file = open(sys.argv[5], 'w')

    # get the initial state from input file
    initial_state = construct_start_state(input_file)

    problem = TileProblem(initial_state, puzzle_size)
    solution = []

    if algorithm == 1:  # a* algorithm
        start_time = datetime.datetime.now()
        a_star = A_star_Algorithm(problem, heuristics)
        solution = a_star.a_star()
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        print(execution_time)
        write_output(out_file, solution)
        print(solution)
    else:  # rbfs algorithm
        start_time = datetime.datetime.now()
        rbfs = Rbfs_Algorithm(problem, heuristics)
        start_node = rbfs.make_node(initial_state, None, None)
        solution, counter  = rbfs.rbfs(start_node, float('inf'))
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        print(execution_time)
        print(solution.actions_till_now)
        print("depth found: ", solution.g_val)
        write_output(out_file, solution.actions_till_now)

    input_file.close()
    out_file.close()
