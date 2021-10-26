class Matrix:
    """
    Representation of a matrix's rows and columns.
    Source: Exercism
    """

    def __init__(self, matrix_string: str):
        """
        Initialises matrix attribute
        matrix_string format: '1 3 1\n4 5 6\n3 1 2'
        """
        self.matrix = [[int(j) for j in i.split()] for i in matrix_string.split('\n')]

    def row(self, index: int) -> list:
        """Returns the indexed row"""
        return self.matrix[index - 1]

    def column(self, index) -> list:
        """Return the indexed column"""
        return list(list(zip(*self.matrix))[index - 1])

    # A lesson on code readability
    def column2(self, index) -> list:
        """Returns the indexed column"""
        return [r[index - 1] for r in self.matrix]    