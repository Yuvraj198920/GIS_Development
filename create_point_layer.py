import arcpy
import sys

def create_sample_feature_layer(gdb_path):
    """Create a sample point feature layer in the given geodatabase."""
    
    # Define the path for the new feature class
    feature_class_path = f"{gdb_path}/SampleLayer"
    
    # Create a new point feature class with the specified fields
    arcpy.CreateFeatureclass_management(
        out_path=gdb_path,
        out_name="SampleLayer",
        geometry_type="POINT",
        spatial_reference=arcpy.SpatialReference(4326)  # Using WGS 1984 spatial reference
    )
    
    # Add fields: ID, Name, Description
    arcpy.AddField_management(feature_class_path, "JobID", "LONG")
    arcpy.AddField_management(feature_class_path, "Name", "TEXT")
    arcpy.AddField_management(feature_class_path, "Description", "TEXT")
    
    # Insert some sample data
    with arcpy.da.InsertCursor(feature_class_path, ["SHAPE@XY", "ID", "Name", "Description"]) as cursor: # type: ignore
        cursor.insertRow([(174.7762, -41.2865), 3, "Point C", "This is Wellington City."])  # Wellington, New Zealand

    print(f"Sample feature layer 'SampleLayer' created in {gdb_path}.")
    return feature_class_path

def update_sde(data, sde_path):
    arcpy.env.workspace = sde_path # type: ignore
    if isinstance(data, str):
        data = int(data)
    row_values = [(174.7762, -41.2865), data]
    fc_list = arcpy.ListFeatureClasses()
    fc_name = ""
    for fc in fc_list: # type: ignore
        fc_name = fc
        desc = arcpy.Describe(fc_name)
        print(desc.shapeType) # type: ignore
    with arcpy.da.InsertCursor(fc_name, ["SHAPE@XY", "JobID"]) as cursor: # type: ignore
        cursor.insertRow([(174.7762, -41.2865), data])
gdb_dir = r"C:\Users\gisuser\Documents\ArcGIS\Packages\Introducing_ArcGIS_Pro_7f7355\sample_gdb.gdb"
sde_path = r"C:\Users\gisuser\Documents\ArcGIS\Projects\vtpk_mmpk_creation\GISDEV.sde"
update_sde(4, sde_path)
    
    
