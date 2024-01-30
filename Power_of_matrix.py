import numpy as np
def Power_of_matrix(matrix,m):
    result = np.linalg.matrix_power(matrix,m)
    return result

Matrix=np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
m=int(input("Enter an integer:"))
result = Power_of_matrix(Matrix,m)
print(f"Matrix A to the power m is: \n {result} ")