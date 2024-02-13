import pandas as pd
import numpy as np
#Q1
data = pd.read_excel('D:\ASEB\Semester 4\ML\Lab3\Lab Session1 Data.xlsx')
A_access =data.iloc[0:10,1:4]
A=A_access.to_numpy()
C_access = data.iloc[:,4]
C=C_access.to_numpy()

Dimensionality_of_A = A.shape
Dimensionality_of_C = C.shape
num_vectors_A = A_access.shape[0]

rank_A =  np.linalg.matrix_rank(A)
print("Matrix A = ",A)
print("Matrix c = ",C)
print("Dimensionality of matrix  vector space: ",Dimensionality_of_A)
print("Dimensionality of matrix C : ",Dimensionality_of_C)
print("Number of vectors in the vector space A : ", num_vectors_A)
print("Rank of matrix A : ", rank_A)

#Q2
X = np.dot(np.linalg.pinv(A),C)
print(X)

#Q3
label = ""
for i in C:
    if (i>200):
        label = "RICH"
    else:
        lable = "POOR"