import arcpy
import os
import sys
from timeit import timeit

# arcpy.env.overwriteOutput = True
@timeit # type: ignore
def get_point_from_id(layer_name, id_value, connection_path):
    arcpy.env.workspace = connection_path # type: ignore
    query = f"ID = {id_value}"
    with arcpy.da.SearchCursor(layer_name, ["SHAPE@"], where_clause = query) as cursor: # type: ignore
        for row in cursor:
            return row[0]
    return None

@timeit # type: ignore
def create_buffer(point_geom, buffer_distance=1000):
    return point_geom.buffer(buffer_distance)

@timeit # type: ignore
def create_mmpk(aprx_file, buffer_feature, dest_folder, id_value):
    aprx = arcpy.mp.ArcGISProject(aprx_file)
    map_obj = aprx.listMaps()[3] # type: ignore
    map_obj.addDataFromPath(buffer_feature)
    mmpk_path = os.path.join(dest_folder, f"buffer_{id_value}.mmpk")
    if arcpy.Exists(mmpk_path):
        print(f"The mmpk for {id_value} already exists.")
    else:
        arcpy.management.CreateMobileMapPackage(map_obj, mmpk_path) # type: ignore

    return mmpk_path

if __name__=='__main__':
    # aprx_file = sys.argv[1]
    # layer_name = sys.argv[2]
    # id_value = int(sys.argv[3])
    # connection_path = sys.argv[4]
    # dest_folder = sys.argv[5]
    # print(sys.argv)

    aprx_file = r"C:\Users\gisuser\Documents\ArcGIS\Packages\Introducing_ArcGIS_Pro_7f7355\p30\Introducing_ArcGIS_Pro.aprx"
    layer_name = "SampleLayer"
    id_value = 3
    connection_path = r"C:\Users\gisuser\Documents\ArcGIS\Packages\Introducing_ArcGIS_Pro_7f7355\sample_gdb.gdb"
    dest_folder = r"C:\Users\gisuser\Documents\ArcGIS\Packages\Introducing_ArcGIS_Pro_7f7355\mmpk"

    try:
        point_geom = get_point_from_id(layer_name, id_value, connection_path) # type: ignore
        buffer_name = "test_buffer_1"
        buffer_path = os.path.join(connection_path, buffer_name)  # Assuming connection_path is the path to your GDB or SDE
        if arcpy.Exists(buffer_path):
            print(f"The buffer file for {buffer_name} already exists.")
        else:
            buff = create_buffer(point_geom, 100) # type: ignore
            arcpy.CopyFeatures_management(buff, buffer_path)
        create_mmpk(aprx_file, buffer_path, dest_folder, id_value) # type: ignore

    except arcpy.ExecuteError:
        print(arcpy.GetMessage(2))
    
    except Exception as e:
        print(e)
