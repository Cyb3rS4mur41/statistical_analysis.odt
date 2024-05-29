
import pandas as pd

def copy_data_to_new_excel(input_file, output_file):
    try:
        # Import Excel file
        excel_data = pd.ExcelFile(input_file)

        # Selecting data from the original file
        df_original = pd.read_excel(excel_data, sheet_name=excel_data.sheet_names[0], header=None)
        selected_data = df_original.iloc[36:109, 0:5]  # Range A37:F110 

        # Create a new Excel file and save the data
        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            selected_data.to_excel(writer, index=False, header=None, startrow=0, startcol=0, sheet_name='Sheet1') # type: ignore

        print(f"The selected data has been successfully copied to the new file: {output_file}")

    except Exception as e:
        print(f"An error occurred while handling files: {str(e)}")

# Original file path
input_file_path = r"path"

# Path to new file
output_file_path = r"path"

# Call a function
copy_data_to_new_excel(input_file_path, output_file_path)
