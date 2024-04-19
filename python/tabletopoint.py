import arcpy
import os

def convert_excel_tables_to_points(cities, years, output_folder_base, gdb_path):
    arcpy.env.overwriteOutput = True
    coordinate_system = ('GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],'
                         'PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];'
                         '-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision')


    for city_prefix, folder_path in cities.items():
        excel_path = os.path.join(folder_path, f"All{city_prefix}Temp.xlsx")  # Path to the Excel file
        for year in years:
            year_suffix = f"{year % 100:02d}"  # Formats the year as two digits
            sheet_name = f"{city_prefix}{year_suffix}$"  # Sheet name in Excel

            # Full table path as expected by ArcGIS
            in_table = f"{excel_path}\\{sheet_name}"

            out_feature_class = os.path.join(gdb_path, f"{city_prefix}{year_suffix}")

            # Check if the Excel file exists before attempting to process
            if os.path.exists(excel_path):
                try:
                    arcpy.management.XYTableToPoint(
                        in_table=in_table,
                        out_feature_class=out_feature_class,
                        x_field="Longitude",
                        y_field="Latitude",
                        z_field=None,
                        coordinate_system=coordinate_system
                    )
                    print(f"Point feature class created for {out_feature_class}")
                except Exception as e:
                    print(f"Failed to convert table to points for {sheet_name}: {str(e)}")
            else:
                print(f"Excel file not found: {excel_path}")

# Configuration for each city
cities = {
    'Austin': 'C:\\778\\778WorkingProject\\austin\\',
    'RDU': 'C:\\778\\778WorkingProject\\raleigh\\',
    'RVA': 'C:\\778\\778WorkingProject\\richmond\\'
}

# Geodatabase path
gdb_path = 'C:\\778\\778WorkingProject\\778WorkingProject.gdb'

# Years to process
years = range(1975, 2021, 5)

# Process each city
convert_excel_tables_to_points(cities, years, cities, gdb_path)
