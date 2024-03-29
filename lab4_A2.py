import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\ASEB\\Semester 4\\ML\\patches_gabor_15816_1 3.csv")

# Choose the feature for analysis (replace 'LocalEnergy_0_1' with the feature you want to analyze)
feature_name = 'LocalEnergy_0_1'
feature_data = df[feature_name].values

# Plot the histogram
plt.hist(feature_data, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title(f'Histogram of {feature_name}')
plt.xlabel(feature_name)
plt.ylabel('Frequency')
plt.show()

# Calculate mean and variance
mean_value = np.mean(feature_data)
variance_value = np.var(feature_data)

print(f"Mean of {feature_name}: {mean_value}")
print(f"Variance of {feature_name}: {variance_value}")
