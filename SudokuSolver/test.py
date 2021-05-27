"""
    This is the structure of our Sudoku problem. Take a note on how crucial parts, (row, columns, and boxes) are
    divided in instances.
"""

from Tile import Cell
import math
import copy
import random


class Test:
    def __init__(self):
        arr = list()

    def recWithStates(self, val):
        if len(val) == 10:
            return True

        valCopy = copy.deepcopy(val)

        value = self.recWithStates(val.add(random.randint(1, 10)))
        if value:
            print('True')
        else:
            print('false')





if __name__ == '__main__':
    initialState = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                    [5, 2, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 7, 0, 0, 0, 0, 3, 1],
                    [0, 0, 3, 0, 1, 0, 0, 8, 0],
                    [9, 0, 0, 8, 6, 3, 0, 0, 5],
                    [0, 5, 0, 0, 9, 0, 6, 0, 0],
                    [1, 3, 0, 0, 0, 0, 2, 5, 0],
                    [0, 0, 0, 0, 0, 0, 0, 7, 4],
                    [0, 0, 5, 2, 0, 6, 3, 0, 0]]


    copied = copy.deepcopy(initialState)

    initialState[0][1] = 11

    print(copied[0][1])
