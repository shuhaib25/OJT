import numpy as np

matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_diagonal_3x3 = np.trace(matrix_3x3)
print("Sum of diagonal elements (3x3):", sum_diagonal_3x3)

matrix_4x4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
sum_diagonal_4x4 = np.trace(matrix_4x4)
print("Sum of diagonal elements (4x4):", sum_diagonal_4x4)
