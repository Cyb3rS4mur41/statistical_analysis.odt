
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_boxplot_with_error(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, sheet_name='Sheet1', header=None)

        # Calculating the standard error
        std_errors = df.iloc[:, 1:].sem()

        # Making boxplot
        sns.set(style="whitegrid")  # Style setting
        ax = sns.boxplot(data=df.iloc[:, 1:], showmeans=True, meanline=True, palette='Set3')

        # Add standard errors to the boxplot
        for i, std_error in enumerate(std_errors):
            ax.errorbar(x=i, y=df.iloc[:, i+1].mean(), yerr=std_error, color='black', capsize=5, capthick=2)

        plt.title('boxplot title')
        plt.xlabel('Name of the x label')
        plt.ylabel('name of the y label')
        plt.show()

    except Exception as e:
        print(f"An error occurred while reading the file or creating the chart: {str(e)}")

# File name or path
file_path = r"path"

# Call a function
plot_boxplot_with_error(file_path)