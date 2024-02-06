import numpy as np
import math
def Euclidean_distance(v1,v2):
    if (len(v1)!=len(v2)):
        raise("Distance can not be calculated for vectors with different domensions.")
    else:
        vector_diff = v1-v2
        vector_diff_square = vector_diff**2
        sum = np.sum(vector_diff_square)
        final_val = math.sqrt(sum)

    return final_val
def Manhatten_distance(v1,v2):
    if (len(v1)!=len(v2)):
        raise("Distance can not be calculated for vectors with different domensions.")
    else:
        vector_diff = abs(v1-v2)
        sum = np.sum(vector_diff)
        final_val = sum
    return final_val

vector1 = [1,2,3]
vector2 = [4,5,6]
vector1_np = np.array(vector1)
vector2_np = np.array(vector2)

result1 = Euclidean_distance(vector1_np,vector2_np)
result2 = Manhatten_distance(vector1_np,vector2_np)
print("The Manhatten distance of both the vectors are: ",result2)
print("The Euclidean distance of both the vectors are: ",result1)