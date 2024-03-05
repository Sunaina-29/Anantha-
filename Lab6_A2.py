import numpy as np
import matplotlib.pyplot as plt

# Initial weights as provided in the image
weights = np.array([-10, -0.2, 0.75])
learning_rate = 0.05

# Reshape the weights vector to make it a column vector
weights = weights.reshape(-1, 1)

# Define the activation functions
def unit_step(x):
    return np.where(x >= 0, 1, 0)

def bipolar_step(x):
    return np.where(x >= 0, 1, -1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

# Training data for AND gate
inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
targets = np.array([0, 0, 0, 1])

# Initialize errors list to store the sum-squared error after each epoch
errors = {}  # Dictionary to store errors for each activation function

# Loop for a fixed number of epochs (e.g., 100)
for epoch in range(100):
    for activation_func_name, activation_func in [
        ("Unit Step", unit_step), ("Bipolar Step", bipolar_step),
        ("Sigmoid", sigmoid), ("ReLU", relu)]:
        total_error = 0
        for i, input in enumerate(inputs):
            # Calculate the linear output
            linear_output = np.dot(weights[1:].T, input) + weights[0]  # Add bias weight

            # Apply the activation function
            predicted = activation_func(linear_output)

            # Calculate the error
            error = targets[i] - predicted

            # Update weights using the learning rule
            weights[1:] += learning_rate * error * input
            weights[0] += learning_rate * error

            # Update total error for this epoch
            total_error += error**2

        # Append the total error of this epoch to the errors list for this activation function
        errors.setdefault(activation_func_name, []).append(total_error)

# Plot the epochs vs errors for each activation function
plt.figure(figsize=(10, 6))
for name, error_list in errors.items():
    plt.plot(range(100), error_list, label=name)
plt.xlabel('Epochs')
plt.ylabel('Sum-Squared Error')
plt.title('Sum-Squared Error per Epoch for AND Gate Perceptron (Different Activations)')
plt.grid(True)
plt.legend()
plt.show()

# Test the trained perceptron on unseen data
test_input1 = np.array([0, 1])
test_input2 = np.array([1, 0])

for activation_func_name, activation_func in [
    ("Unit Step", unit_step), ("Bipolar Step", bipolar_step),
    ("Sigmoid", sigmoid), ("ReLU", relu)]:
    predicted_output1 = activation_func(np.dot(weights[1:].T, test_input1) + weights[0])
    predicted_output2 = activation_func(np.dot(weights[1:].T, test_input2) + weights[0])
    print(f"Predicted output for [0, 1] using {activation_func_name}: {predicted_output1}")
    print(f"Predicted output for [1, 0] using {activation_func_name}: {predicted_output2}")