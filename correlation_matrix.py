
import pandas as pd

def correlation_matrix(file_path):
    try:
        # Read an Excel file, only the range B1:E74
        df = pd.read_excel(file_path, usecols="B:E", skiprows=1, nrows=74)

        # Creating a correlation matrix
        correlation_matrix = df.corr()

        print("The correlation matrix:")
        print(correlation_matrix)

    except Exception as e:
        print(f"An error occurred while reading the file or creating the correlation matrix: {str(e)}")

# File name or path
file_path = r"path"

# Call a function
correlation_matrix(file_path)

