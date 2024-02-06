import numpy as np

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def k_nearest_neighbors(train_data, train_labels, test_point, k):
    distances = []

    # Calculate distances between test_point and all training data points
    for i in range(len(train_data)):
        dist = euclidean_distance(test_point, train_data[i])
        distances.append((dist, train_labels[i]))

    # Sort distances and get the k-nearest neighbors
    sorted_distances = sorted(distances, key=lambda x: x[0])
    neighbors = sorted_distances[:k]

    # Count the occurrences of each label among the k-nearest neighbors
    label_counts = {}
    for neighbor in neighbors:
        label = neighbor[1]
        label_counts[label] = label_counts.get(label, 0) + 1

    # Find the label with the highest count
    predicted_label = max(label_counts, key=label_counts.get)

    return predicted_label
# Assuming train_data and train_labels are your training dataset and labels
train_data = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
train_labels = np.array(['A', 'B', 'A', 'B'])
test_point = np.array([2.5, 3.5])
k_value = 3

prediction = k_nearest_neighbors(train_data, train_labels, test_point, k_value)
print(f"The predicted label for the test point is: {prediction}")
