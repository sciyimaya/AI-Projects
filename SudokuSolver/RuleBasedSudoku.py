import copy
from Sudoku import Sudoku


class RuleBasedSudoku:

    """
        Backtracking function to find a solution.
    """
    def solveProblem(self, problem: Sudoku):
        # Fill in all the possible tiles with educated predictions.
        while True:
            if self.applyNakedSingle(problem):
                continue
            if self.applyNakedTuple(problem):
                continue
            break

        # Check if we find the solution after applying Sudoku.
        if self.goalTest(problem):
            return problem

        # Save updated state of the problem before making guesses with candidates.
        beforeUpdateProblem = copy.deepcopy(problem)

        # Backtrack from populated sudoku problem
        tile = self.findMostConstrainedTile(problem)
        for index in range(len(tile.candidates)):
            if not problem.isConflicting(tile.candidates[index], rowIndex=tile.rowIndex, colIndex=tile.colIndex):
                problem.assignValue(value=tile.candidates[index], row=tile.rowIndex, col=tile.colIndex)
                updatedProblem = self.solveProblem(problem)
                if self.goalTest(updatedProblem):
                    return updatedProblem
                else:
                    problem = beforeUpdateProblem
                    tile = problem.state[tile.rowIndex][tile.colIndex]
        # No candidates, Hit dead end
        return None

    """
        For all the tiles that has only 1 value in their candidates, assigns it to the tile.
    """
    def applyNakedSingle(self, problem):
        couldApply = False
        for row in range(9):
            for col in range(9):
                cell = problem.state[row][col]
                if cell.value == 0 and len(cell.candidates) == 1:
                    problem.assignValue(value=cell.candidates[0], row=cell.rowIndex, col=cell.colIndex)
                    couldApply = True
        return couldApply

    """
        A naked pair is set of two candiates that placed in two tiles that belongs to at least one unit in common, that
        is either row, column or box. It is clear that each tile will take either one of those candidates, so we remove
        those candidates from other empty tiles in possible units.
    """
    def applyNakedTuple(self, problem):
        couldApply = False
        # Check every row and look for a naked tuple. If found one, update entire row accordingly.
        if self.nakedTupleUnit(problem.getRows()):
            couldApply = True
        # Check every column and look for a naked tuple. If found one, update entire column accordingly.
        if self.nakedTupleUnit(problem.getCols()):
            couldApply = True
        # Check every box and look for a naked tuple. If found one, update entire box accordingly.
        if self.nakedTupleUnit(problem.getBoxes()):
            couldApply = True
        return couldApply

    """
        For each unit in the problem, look for naked tuples and update units accordingly.
    """
    def nakedTupleUnit(self, units):
        for unit in units:
            # filter the unit by their candidate numbers(being 2), and sort them by the values in ascending order.
            tuples = sorted(
                filter(lambda cellNode: len(cellNode.candidates) == 2, unit),
                key=lambda cellNode: cellNode.candidates)
            if len(tuples) > 1:
                for index in range(len(tuples) - 1):
                    if tuples[index].candidates == tuples[index + 1].candidates:
                        return self.removeFromUnit(unit, tuples[index].candidates, [tuples[index], tuples[index+1]])

    """
        remove the passed candidates from all unassigned tiles in given unit, except index and index + 1th tiles. 
    """
    def removeFromUnit(self, unit, candidates, ignoreList):
        removed = False
        for i in range(9):
            if unit[i] not in ignoreList:
                if candidates[0] in unit[i].candidates:
                    unit[i].candidates.remove(candidates[0])
                    removed = True
                if candidates[1] in unit[i].candidates:
                    unit[i].candidates.remove(candidates[1])
                    removed = True
        return removed


    """
        Finds the most constrained cell in the problem
    """
    def findMostConstrainedTile(self, problem):
        unassignedCells = list()
        for row in problem.getRows():
            for cell in row:
                if cell.value == 0:
                    unassignedCells.append(cell)

        return sorted(unassignedCells, key=lambda cell: len(cell.candidates))[0]


    """
        Method to check if sudoku is completed.
    """
    def goalTest(self, problem: Sudoku):
        if problem is None:
            return False
        for row in range(0, 9):
            for col in range(0, 9):
                if problem.state[row][col].value == 0:
                    return False
        return True