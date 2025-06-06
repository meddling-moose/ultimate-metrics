import pandas as pd
import os
import argparse

INPUT_PATH = 'data/raw/pbr_roundrobin_6_1_2025.xlsx'

def convert_excel_to_csv(input_path, output_dir='data/processed'):
    excel_file = pd.ExcelFile(input_path)
    print(f"Found sheets: {excel_file.sheet_names}")

    os.makedirs(output_dir, exist_ok=True)

    for sheet in excel_file.sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet)
        # Remove unnamed columns
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        filename = f"{sheet.replace(' ', '_').lower()}.csv"
        output_path =os.path.join(output_dir, filename)

        df.to_csv(output_path, index=False)
        print(f"Saved {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Excel sheets to individual CSV files.")
    parser.add_argument("--input", required=True, help="Path to the Excel file (e.g. data/raw/myfile.xlsx)")
    parser.add_argument("--ouput", default="data/processed", help="Output directory for CSVs")

    args = parser.parse_args()
    convert_excel_to_csv(args.input)