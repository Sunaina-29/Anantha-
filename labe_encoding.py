def label_encode_categorical(data):
    unique_labels = {}  # Dictionary to store unique labels with corresponding numeric values
    encoded_data = []   # List to store the encoded values for each data point

    for category in data:
        if category not in unique_labels:
            # Assign a new numeric value for the unseen category
            unique_labels[category] = len(unique_labels)
        
        # Append the numeric value to the encoded data list
        encoded_data.append(unique_labels[category])

    return encoded_data, unique_labels

# Example usage:
categorical_data = ["O", "A+", "A", "A+", "F", "B", "B+", "A+", "B+", "B", "A"]
encoded_data, label_mapping = label_encode_categorical(categorical_data)

print("Original categorical data:", categorical_data)
print("Encoded data:", encoded_data)
print("Label mapping:", label_mapping)


