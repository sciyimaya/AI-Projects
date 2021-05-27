"""
    This is the structure of our Sudoku problem. Take a note on how crucial parts, (row, columns, and boxes) are
    divided in instances.
"""

from Tile import Cell


class Sudoku:

    def __init__(self, state):
        self.state = self.setState(state)
        self.populateCandidates()

    """
        Convert given values in the array to Cell objects
    """
    def setState(self, state):
        rows = list()
        for rowIndex in range(9):
            row = list()
            for colIndex in range(9):
                row.append(Cell(rowIndex=rowIndex, colIndex=colIndex, value=state[rowIndex][colIndex]))
            rows.append(row)
        return rows

    """
        Return an array that contains rows in the Sudoku problem as an array of Cells
    """
    def getRows(self):
        rows = list()
        for rowIndex in range(9):
            row = list()
            for colIndex in range(9):
                row.append(self.state[rowIndex][colIndex])
            rows.append(row)
        return rows

    """
        Return an array that contains columns in the Sudoku problem as an array of Cells
    """
    def getCols(self):
        columns = list()
        for rowIndex in range(9):
            col = list()
            for colIndex in range(9):
                col.append(self.state[colIndex][rowIndex])
            columns.append(col)

        return columns

    """
        Return an array that contains boxes in the Sudoku problem as an array of Cells
    """
    def getBoxes(self):
        boxes = list()
        for outterRowIndex in range(3):
            for outterColIndex in range(3):
                box = list()
                for rowIndex in range(outterRowIndex * 3, outterRowIndex * 3 + 3):
                    for colIndex in range(outterColIndex * 3, outterColIndex * 3 + 3):
                        box.append(self.state[rowIndex][colIndex])
                boxes.append(box)

        return boxes

    """
        For each Cell in the problem, construct their candidates accordingly until we haven't updated any tile candidate.
    """
    def populateCandidates(self):
        updated = False
        # For every tile in the problem,
        for row in range(9):
            for col in range(9):
                # If the tile has no value, update its candidates accordingly
                cell = self.state[row][col]
                if cell.value == 0:
                    updated = self.updateCandRows(cell, row) if not updated else True
                    updated = self.updateCandColumns(cell, col) if not updated else True
                    updated = self.updateCandBoxes(cell, row, col) if not updated else True
        if not updated:
            return
        else:
            self.populateCandidates()


    """
        Populate all the unassigned tile's candidates in given row accordingly.
    """
    def updateCandRows(self, cell: Cell, row: int):
        updated = False
        rows = self.getRows()
        # for every tile in this row,
        for colIndex in range(9):
            currentTile = rows[row][colIndex]
            # update passed tile's candidates based on tiles that has values
            if currentTile.value != 0 and currentTile.value in cell.candidates:
                updated = True
                cell.candidates.remove(currentTile.value)
        return updated

    """
        Populate all the unassigned tile's candidates in given column accordingly.
    """
    def updateCandColumns(self, cell: Cell, col: int):
        updated = False
        cols = self.getCols()
        # for every tile in this column,
        for rowIndex in range(9):
            currentTile = cols[col][rowIndex]
            # update passed tile's candidates based on tiles that has values
            if currentTile.value != 0 and currentTile.value in cell.candidates:
                updated = True
                cell.candidates.remove(currentTile.value)
        return updated

    """
        Populate all the unassigned tile's candidates in the associated box accordingly.
    """
    def updateCandBoxes(self, cell: Cell, row: int, col: int):
        updated = False
        boxes = self.getBoxes()
        boxNum = int(row/3)*3 + int(col/3)
        # for every tile in this box,
        for index in range(9):
            currentTile = boxes[boxNum][index]
            # update passed tile's candidates based on tiles that has values
            if currentTile.value != 0 and currentTile.value in cell.candidates:
                updated = True
                cell.candidates.remove(currentTile.value)
        return updated
    """
        Method to use when assigning values to tiles in the sudoku.
        After assigning value, updates candidates of empty tiles in same row, column and box accordingly.
    """
    def assignValue(self, value, row, col):
        self.state[row][col].setValue(value)
        self.populateCandidates()
        return True

    """
        Check if given value can be assigned to the specified location on the sudoku.
    """
    def isConflicting(self, value, rowIndex, colIndex):
        # Check row consistency
        row = self.getRows()[rowIndex]
        for cell in row:
            if cell.value == value:
                return True
        # Check col consistency
        col = self.getCols()[colIndex]
        for cell in col:
            if cell.value == value:
                return True
        # Check box consistency
        box = self.getBoxes()[int(rowIndex/3)*3 + int(colIndex/3)]
        for cell in box:
            if cell.value == value:
                return True
        return False

    """
        Return stringified format of the sudoku 
    """
    def getSolution(self):
        output = ''
        for row in self.getRows():
            strippedRow = ''
            for cell in row:
                strippedRow += str(cell.value) if cell.value != 0 else ' '
                strippedRow += ' '
            output += strippedRow
            output += '\n'
        return output
