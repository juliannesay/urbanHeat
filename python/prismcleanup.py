import pandas as pd

def process_city_data(file_path, output_folder, city_prefix):
    # Load the CSV file for the city
    df = pd.read_csv(file_path)

    # Drop rows where 'Date' is NaN
    df = df.dropna(subset=['Date'])

    # Set up an Excel writer for the combined yearly data
    all_data_excel_filename = f"{output_folder}All{city_prefix}Temp.xlsx"
    excel_writer = pd.ExcelWriter(all_data_excel_filename, engine='openpyxl')

    # Process each year
    years = range(1975, 2021, 5)  # From 1975 through 2020, in increments of 5 years
    for year in years:
        # Format year to ensure it's always two digits (e.g., '00' instead of '0' for 2000)
        year_suffix = f"{year % 100:02d}"  # Formats the year as two digits

        # Filter rows where 'Date' column starts with the specific year and month 'YYYY-07'
        year_df = df[df['Date'].str.startswith(f'{year}-07')]

        # Define file names for CSV and Excel
        csv_filename = f"{output_folder}{city_prefix}{year_suffix}.csv"
        excel_filename = f"{output_folder}{city_prefix}{year_suffix}.xlsx"
        
        # Save to CSV, overwrite if exists
        year_df.to_csv(csv_filename, index=False, mode='w')
        # Save to Excel, overwrite if exists
        year_df.to_excel(excel_filename, index=False, engine='openpyxl')

        # Also append to the combined Excel file
        year_df.to_excel(excel_writer, index=False, sheet_name=f"{city_prefix}{year_suffix}")

        print(f"Files for {city_prefix}{year} processed and saved: CSV and Excel.")

    # Save and close the Excel writer
    excel_writer.save()
    excel_writer.close()

# File paths and directories for each city
austin_file = 'C:\\778\\PRISMAUSTIN.csv'
raleigh_file = 'C:\\778\\PRISMRDU.csv'
richmond_file = 'C:\\778\\PRISMRVA.csv'

austin_output = 'C:\\778\\778WorkingProject\\austin\\'
raleigh_output = 'C:\\778\\778WorkingProject\\raleigh\\'
richmond_output = 'C:\\778\\778WorkingProject\\richmond\\'

# Process each city's data
process_city_data(austin_file, austin_output, 'Austin')
process_city_data(raleigh_file, raleigh_output, 'RDU')
process_city_data(richmond_file, richmond_output, 'RVA')
