import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

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

# Vary k from 1 to 11
k_values = np.arange(1, 12)
accuracy_nn = []  # to store accuracy for NN classifier
accuracy_knn3 = []  # to store accuracy for kNN classifier with k=3

for k in k_values:
    # NN classifier
    nn_classifier = KNeighborsClassifier(n_neighbors=k)
    nn_classifier.fit(X_train, y_train)
    y_pred_nn = nn_classifier.predict(X_test)
    accuracy_nn.append(accuracy_score(y_test, y_pred_nn))

    # kNN classifier with k=3
    knn_classifier = KNeighborsClassifier(n_neighbors=3)
    knn_classifier.fit(X_train, y_train)
    y_pred_knn3 = knn_classifier.predict(X_test)
    accuracy_knn3.append(accuracy_score(y_test, y_pred_knn3))

# Plot the results
plt.plot(k_values, accuracy_nn, label='NN (k varying)')
plt.plot(k_values, accuracy_knn3, label='kNN (k=3)')
plt.title('Accuracy Comparison for NN and kNN (k=3)')
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
