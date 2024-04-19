import arcpy
from arcpy.sa import Kriging, KrigingModelOrdinary, KrigingModelUniversal

def perform_kriging(cities, years, gdb_path):
    # Check out the Spatial Analyst extension
    arcpy.CheckOutExtension("Spatial")
    arcpy.env.overwriteOutput = True

    for city_prefix, folder_path in cities.items():
        for year in years:
            year_suffix = f"{year % 100:02d}"  # Formats the year as two digits
            point_feature_class = f"{gdb_path}\\{city_prefix}{year_suffix}"
            output_raster_name = f"{city_prefix}{year_suffix}Krig"

            # Kriging tool parameters
            z_field = "mtemp"
            model = KrigingModelOrdinary("Spherical")
            cell_size = 0.00542600000000016
            search_radius = arcpy.sa.RadiusVariable(12)

            out_surface_raster = Kriging(
                in_point_features=point_feature_class,
                z_field=z_field,
                kriging_model=model,
                cell_size=cell_size,
                search_radius=search_radius
            )

            # Save the output raster to the geodatabase
            out_surface_raster.save(f"{gdb_path}\\{output_raster_name}")
            print(f"Kriging surface created and saved as: {output_raster_name}")

    # Check in the Spatial Analyst extension after processing
    arcpy.CheckInExtension("Spatial")

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

# Execute Kriging
perform_kriging(cities, years, gdb_path)
