import pandas as pd


def change_to_csv(input_file):
    # input_file = "MachineLearningRating_v3.txt"  
    output_file = "../../Data/MachineLearningRating_v3/MachineLearningRating_v3.csv" 

    data = pd.read_csv(input_file, delimiter='|') # Delimeter


    data.to_csv(output_file, index=False)

    print(f"File successfully converted and saved as {output_file}")
    return output_file


def load_data(filepath):
    """Load data from a CSV or TXT file."""
    return pd.read_csv(filepath)

def check_data_types(df):
    """Check data types of each column."""
    return df.dtypes

def check_missing_values(df):
    """Check for missing values in the DataFrame."""
    return df.isnull().sum()