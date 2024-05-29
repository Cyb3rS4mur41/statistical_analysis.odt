
import pandas as pd

def descriptive_statistics(file_path):
    try:
        # Import Excel file
        df = pd.read_excel(file_path)

        # Preparation of descriptive statistics
        statistics = df.describe()

        # Addition of mode, since describe does not include it
        statistics.loc['mode'] = df.mode().iloc[0]

        # Calculation of interquartile range
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        statistics.loc['iqr'] = IQR

        print(statistics)

    except Exception as e:
        print(f"An error occurred while reading the file or creating statistics: {str(e)}")

# File name or path
file_path = r"path"

# Call a function
descriptive_statistics(file_path)


