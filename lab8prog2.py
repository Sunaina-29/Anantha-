import pandas as pd

# Assuming the dataset is stored in a CSV file named 'dataset.csv'
data = pd.read_csv(r"D:\ASEB\Semester 4\ML\Lab8\patches_gabor_15816_1 3.csv")

def binning(data, num_bins=None, binning_type='equal_width'):
    """
    Bins continuous-valued attributes into categorical-valued attributes using equal width or frequency binning.

    Parameters:
        data (DataFrame): Input data with continuous-valued attributes.
        num_bins (int): Number of bins to create. If None, will be set to sqrt(n), where n is the number of data points.
        binning_type (str): Type of binning to perform. Options are 'equal_width' or 'frequency'.

    Returns:
        DataFrame: Data with continuous attributes replaced by categorical attributes.
    """
    # Default number of bins
    if num_bins is None:
        num_bins = int(len(data) ** 0.5)

    # Perform equal width binning
    if binning_type == 'equal_width':
        for column in data.columns:
            if data[column].dtype != 'object':  # Only process numerical attributes
                data[column] = pd.cut(data[column], bins=num_bins, labels=False)
    
    # Perform frequency binning
    elif binning_type == 'frequency':
        for column in data.columns:
            if data[column].dtype != 'object':  # Only process numerical attributes
                data[column] = pd.qcut(data[column], q=num_bins, labels=False, duplicates='drop')

    return data

# Binning the dataset with default parameters
data_binned = binning(data)

# Export the binned dataset to a CSV file
data_binned.to_csv(r"D:\ASEB\Semester 4\ML\Lab8\binned.csv", index=False)

print("Binned dataset exported successfully!")
