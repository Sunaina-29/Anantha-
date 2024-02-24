import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("D:\ASEB\Semester 4\ML\patches_gabor_15816_1 3.csv")

X = df.iloc[ : , 1:-1].values
y = df.iloc[ : , -1].values

X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size=0.3)
print(f"X_train shape: {X_train1.shape}")
print(f"X_test shape: {X_test1.shape}")
print(f"y_train shape: {y_train1.shape}")
print(f"y_test shape: {y_test1.shape}")
print("\n---------\n")

class_label1 = 'bad'
class_label2 = 'medium'

# Select rows corresponding to the chosen classes
class_data = df[(df['class'] == class_label1) | (df['class'] == class_label2)]

# Features and class labels for the chosen classes
X_selected = class_data.iloc[:, 1:-1].values
y_selected = class_data.iloc[:, -1].values

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y_selected, test_size=0.3, random_state=42)

# Print the shapes of the resulting sets
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

