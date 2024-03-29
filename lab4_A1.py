import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\ASEB\\Semester 4\\ML\\patches_gabor_15816_1 3.csv")

# Assuming the columns are features and the last column is the class label
X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values

# Function to calculate mean and standard deviation for each class
def calculate_class_stats(X, y, class_label):
    class_indices = np.where(y == class_label)
    class_data = X[class_indices]

    class_mean = np.mean(class_data, axis=0)
    class_std = np.std(class_data, axis=0)

    return class_mean, class_std

# Function to calculate Euclidean distance between class centroids
def calculate_distance(centroid1, centroid2):
    return np.linalg.norm(centroid1 - centroid2)

# Choose two classes for evaluation (replace 0 and 1 with your actual class labels)
class_label1 = 'bad'
class_label2 = 'medium'

# Calculate mean and standard deviation for each class
centroid1, std1 = calculate_class_stats(X, y, class_label1)
centroid2, std2 = calculate_class_stats(X, y, class_label2)

# Calculate Euclidean distance between class centroids
distance_between_classes = calculate_distance(centroid1, centroid2)

# Print the results
print(f"Mean vector for class {class_label1}: {centroid1}")
print(f"Standard deviation vector for class {class_label1}: {std1}")
print()
print(f"Mean vector for class {class_label2}: {centroid2}")
print(f"Standard deviation vector for class {class_label2}: {std2}")
print()
print(f"Distance between class centroids: {distance_between_classes}")

#---------------------------------------------------------------------------------------



