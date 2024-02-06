def one_hot_encode(categories):
    unique_categories = list(set(categories))
    num_categories = len(unique_categories)
    
    encoded_matrix = []
    
    for category in categories:
        encoded_vector = [0] * num_categories
        category_index = unique_categories.index(category)
        encoded_vector[category_index] = 1
        encoded_matrix.append(encoded_vector)
    
    return encoded_matrix, unique_categories

# Example usage:
categories = ['red', 'blue', 'green', 'red', 'green']

encoded_matrix, unique_categories = one_hot_encode(categories)

print("One-Hot Encoded Matrix:")
for encoded_vector in encoded_matrix:
    print(encoded_vector)

print("\nUnique Categories:", unique_categories)
