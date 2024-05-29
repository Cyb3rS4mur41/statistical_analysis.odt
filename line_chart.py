
import pandas as pd
import matplotlib.pyplot as plt

def plot_line_chart(file_path):
    try:
        # Read Excel file
        df = pd.read_excel(file_path, sheet_name='Sheet1', header=None)

        # The values of the x-axis
        x_values = df.iloc[:, 0]

        # The values ​​of the lines are from the different columns
        y_values_b = df.iloc[:, 1]
        y_values_c = df.iloc[:, 2]
        y_values_d = df.iloc[:, 3]
        y_values_e = df.iloc[:, 4]

        # Making a line diagram
        plt.plot(x_values, y_values_b, marker='o', linestyle='-', color='b', label='label1')
        plt.plot(x_values, y_values_c, marker='o', linestyle='-', color='g', label='label2')
        plt.plot(x_values, y_values_d, marker='o', linestyle='-', color='r', label='label3')
        plt.plot(x_values, y_values_e, marker='o', linestyle='-', color='purple', label='label4')

        plt.title('Title of the legend')
        plt.xlabel('name of the x label')
        plt.ylabel('name of the y label')
        plt.legend()  # Add the legend
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"An error occurred while reading the file or creating the chart: {str(e)}")

# File name or path
file_path = "path"

# Call a function
plot_line_chart(file_path)

