import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("D:\ASEB\Semester 4\ML\patches_gabor_15816_1 3.csv")

X = df.iloc[ : , 1:-1].values
y = df.iloc[ : , -1].values

class_label1 = 'bad'
class_label2 = 'medium'

# Select rows corresponding to the chosen classes
class_data = df[(df['class'] == class_label1) | (df['class'] == class_label2)]

# Features and class labels for the chosen classes
X_selected = class_data.iloc[:, 1:-1].values
y_selected = class_data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X_selected, y_selected, test_size=0.3, random_state=42)

# Create a kNN classifier with k=3
knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Train the classifier on the training set
knn_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = knn_classifier.predict(X_test)

# Calculate and print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of kNN classifier with k=3: {accuracy}")
