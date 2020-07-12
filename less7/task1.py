class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(str(el) for el in self.matrix)

    def __add__(self, other):
        result = self.__class__(
            [
                ([self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))])
                for i in range(len(self.matrix))
            ]
        )
        return result


matrix1 = [
    [2, 3, 4],
    [4, 5, 4],
    [3, 2, 1]
]
matrix2 = [
    [7, 4, 8],
    [5, 1, 9],
    [7, 2, 3]
]
matrix3 = [
    [2, 3, 5],
    [5, 3, 6],
    [4, 2, 1]
]
a = Matrix(matrix1)
b = Matrix(matrix2)
c = Matrix(matrix3)

print(a + b + c)
