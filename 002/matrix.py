# This Exercism taught me a lot about list comprehensions and zip functions

class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(j) for j in i.split()] for i in matrix_string.split('\n')]
    def row(self, index):
        return self.matrix[index - 1]
    def column(self, index):
        return list(list(zip(*self.matrix))[index - 1])

    # A lesson on code readability
    def column2(self, index):
        return [r[index - 1] for r in self.matrix]    