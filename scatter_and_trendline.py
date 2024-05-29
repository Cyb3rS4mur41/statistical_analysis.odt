import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

def plot_scatter_with_trendline(file_path):
    try:
        # Read  the Excel file
        df = pd.read_excel(file_path, sheet_name='Sheet1', header=None)

        # Creating a scatter plot
        sns.set(style="whitegrid")  # Style setting
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=df.iloc[:, 0], y=df.iloc[:, 1], color='skyblue')

        # Add a trend line
        slope, intercept, r_value, p_value, std_err = linregress(df.iloc[:, 0], df.iloc[:, 1])
        line = slope * df.iloc[:, 0] + intercept
        plt.plot(df.iloc[:, 0], line, color='black', label='Trendline')

        plt.title('name of the scatter plot')
        plt.xlabel('name of the x label')
        plt.ylabel('name of the y label')
        plt.show()

    except Exception as e:
        print(f"An error occurred while reading the file or creating the chart: {str(e)}")

# File name or path
file_path = r"path"

# Call a function
plot_scatter_with_trendline(file_path)