import numpy as np
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])


add_result = np.add(matrix1, matrix2)

sub_result = np.subtract(matrix1, matrix2)

mul_result = np.dot(matrix1, matrix2)

print("\nMatrix Addition:")
print(add_result)
print("\nMatrix Subtraction:")
print(sub_result)
print("\nMatrix Multiplication:")
print(mul_result)
