import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import minkowski

df = pd.read_csv("D:\\ASEB\\Semester 4\\ML\\patches_gabor_15816_1 3.csv")

# Choose any two feature vectors (replace 0 and 1 with the indices of the vectors you want to compare)
vector1 = df.iloc[0, 1:-1].values
vector2 = df.iloc[1, 1:-1].values

# Calculate Minkowski distances for varying values of r from 1 to 10
r_values = np.arange(1, 11)
distances = [minkowski(vector1, vector2, p=r) for r in r_values]

# Plot the distances
plt.plot(r_values, distances, marker='o', linestyle='-')
plt.title('Minkowski Distance vs. r')
plt.xlabel('r')
plt.ylabel('Minkowski Distance')
plt.show()
