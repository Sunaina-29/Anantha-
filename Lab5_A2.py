import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load data from Excel sheet
excel_file = 'D:\ASEB\Semester 4\ML\Lab Session1 Data.xlsx'  # Update with the actual path to your Excel file
df = pd.read_excel(excel_file)

# Convert 'Price' column to numeric
df['Price'] = pd.to_numeric(df['Price'].str.replace(',', ''), errors='coerce')

# Assuming you have a column 'Predicted' with your predicted prices, replace it with your actual case
# For the purpose of the example, let's create a 'Predicted' column with random values for demonstration
df['Predicted'] = np.random.uniform(df['Price'].min(), df['Price'].max(), size=len(df))

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(df['Price'], df['Predicted'])

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)

# Calculate Mean Absolute Percentage Error (MAPE)
mape = np.mean(np.abs((df['Price'] - df['Predicted']) / df['Price'])) * 100

# Calculate R-squared (R2)
r2 = r2_score(df['Price'], df['Predicted'])

# Print the results
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'Mean Absolute Percentage Error (MAPE): {mape}')
print(f'R-squared (R2): {r2}')
