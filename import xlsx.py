
import pandas as pd

def read_excel_sheets(file_path):
    try:
        # Read the Excel file
        excel_data = pd.ExcelFile(file_path)

        # Check: how many sheets are in the Excel file
        sheet_names = excel_data.sheet_names
        num_sheets = len(sheet_names)

        if num_sheets == 0:
            print("A fájl nem tartalmaz sheet-et.")
        else:
            print(f"A fájl {num_sheets} sheet-et tartalmaz. Sheet-ek nevei:")

            # Writing sheet names
            for sheet_name in sheet_names:
                print(f"- {sheet_name}")

    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")

# File path
file_path = r"path"

# Call a function
read_excel_sheets(file_path)

