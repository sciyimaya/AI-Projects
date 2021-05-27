"""
    This class contains details regarding each cell structure
"""

class Cell:

    def __init__(self, rowIndex, colIndex, value=0):
        self.rowIndex = rowIndex
        self.colIndex = colIndex
        self.value = value
        self.candidates = [i for i in range(1, 10)] if value == 0 else []

    def setValue(self, value):
        if value in self.candidates:
            self.value = value
            self.candidates.clear()
        else:
            raise ValueError("Passed value", value, "is not a candidate for this cell.")

    def __str__(self):
        return self.value
