import sys


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.result = []
        self.rows_of_matrix = len(self.matrix)
        self.columns_of_matrix = len(self.matrix[0])

    def __str__(self):
        rows_string = ""
        for row in self.matrix:
            rows_string += f"{row}\n"
        return rows_string

    def __add__(self, other):
        max_rows = self.__count_max_rows(other)
        max_columns = self.__count_max_columns(other)
        self.__create_blank_matrix(max_rows, max_columns)
        self.__adjust_matrices(other, max_rows, max_columns)
        for i in range(self.rows_of_matrix):
            for j in range(self.columns_of_matrix):
                self.result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.result)

    def __sub__(self, other):
        max_rows = self.__count_max_rows(other)
        max_columns = self.__count_max_columns(other)
        self.__create_blank_matrix(max_rows, max_columns)
        self.__adjust_matrices(other, max_rows, max_columns)
        for i in range(self.rows_of_matrix):
            for j in range(self.columns_of_matrix):
                self.result[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(self.result)

    def __mul__(self, other):
        try:
            if self.rows_of_matrix > other.columns_of_matrix:
                raise ValueError
            elif self.columns_of_matrix > other.rows_of_matrix:
                raise ValueError

            max_rows = self.rows_of_matrix
            max_columns = other.columns_of_matrix
            self.__create_blank_matrix(max_rows, max_columns)
            for i in range(self.rows_of_matrix):
                for j in range(other.columns_of_matrix):
                    for k in range(other.rows_of_matrix):
                        self.result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(self.result)
        except ValueError:
            print("Invalid matrix format for multiplication, e.g. [3x2] * [2x3]", file=sys.stderr)

    def scalar_mul(self, scalar):
        for i in range(self.rows_of_matrix):
            for j in range(self.columns_of_matrix):
                self.matrix[i][j] *= scalar

    def transpose(self):
        max_rows = self.rows_of_matrix
        max_columns = self.columns_of_matrix
        self.__create_blank_matrix(max_rows, max_columns)
        for i in range(self.rows_of_matrix):
            for j in range(self.columns_of_matrix):
                self.result[i][j] = self.matrix[j][i]
        self.matrix = self.result

    def __adjust_matrices(self, other, max_rows, max_columns):
        if self.rows_of_matrix != max_rows:
            new_row = [0 for i in range(max_rows)]
            self.matrix.append(new_row)
        if self.columns_of_matrix != max_columns:
            for row in self.matrix:
                row.append(0)

        if other.rows_of_matrix != max_rows:
            new_row = [0 for i in range(max_rows)]
            other.matrix.append(new_row)
        if other.columns_of_matrix != max_columns:
            for row in other.matrix:
                row.append(0)

    def __create_blank_matrix(self, max_rows, max_columns):
        for i in range(max_rows):
            new_row = [0 for i in range(max_columns)]
            self.result.append(new_row)

    def __count_max_rows(self, other):
        if self.rows_of_matrix > other.rows_of_matrix:
            return self.rows_of_matrix
        else:
            return other.rows_of_matrix

    def __count_max_columns(self, other):
        if self.columns_of_matrix > other.columns_of_matrix:
            return self.columns_of_matrix
        else:
            return other.columns_of_matrix

    def transform_upper_triangle(self):
        self.matrix[0], self.matrix[1] = self.matrix[1], self.matrix[0]
        max_in_row = max(self.matrix[1])
        multiplier = [i * -max_in_row for i in self.matrix[0]]
        for i in range(self.columns_of_matrix):
            self.matrix[1][i] += multiplier[i]
            self.matrix[2][i] += self.matrix[0][i]
        min_in_row = self.matrix[2][1]
        for i in range(self.columns_of_matrix):
            self.matrix[1][i] //= -2
            self.matrix[2][i] //= min_in_row
        self.matrix[1], self.matrix[2] = self.matrix[2], self.matrix[1]
        max_in_row = max(self.matrix[2])
        multiplier = [i * -max_in_row for i in self.matrix[1]]
        for i in range(self.columns_of_matrix):
            self.matrix[2][i] += multiplier[i]


matrix_a = Matrix([[1, 3], [3, 5], [4, 6]])
matrix_b = Matrix([[12, 7, 3], [4, 5, 6], [4, 5, 6]])
matrix_c = Matrix([[4, 2, 0], [1, 3, 2], [-1, 3, 10]])
matrix_c.transform_upper_triangle()
print(matrix_c)