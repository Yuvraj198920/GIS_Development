import logging
import arcpy
import os
import sys
from timeit import timeit

from arcpy_logger import ArcPyLogHandler

logger = logging.getLogger("LoggerName")
handler = ArcPyLogHandler(
        "output_log.log",
        maxBytes=1024 * 1024 * 2, #2MB log files
        backupCount=10
    )
formatter = logging.Formatter("%(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
# arcpy.env.overwriteOutput = True
@timeit # type: ignore
def get_point_from_id(layer_name, id_value, connection_path):
    arcpy.env.workspace = connection_path # type: ignore
    query = f"ID = {id_value}"
    with arcpy.da.SearchCursor(layer_name, ["SHAPE@"], where_clause = query) as cursor: # type: ignore
        print(arcpy.GetMessages(0))
        for row in cursor:
            return row[0]
    return None

@timeit # type: ignore
def create_buffer(point_geom, buffer_distance=1000):
    buf = point_geom.buffer(buffer_distance)
    print(arcpy.GetMessages(0))
    return buf

@timeit # type: ignore
def create_mmpk(aprx_file, buffer_feature, dest_folder, id_value):
    aprx = arcpy.mp.ArcGISProject(aprx_file)
    map_obj = aprx.listMaps()[3] # type: ignore
    map_obj.addDataFromPath(buffer_feature)
    mmpk_path = os.path.join(dest_folder, f"buffer_{id_value}.mmpk")
    if arcpy.Exists(mmpk_path):
        print(arcpy.GetMessages(0))
        print("arcpy message")
        print(arcpy.GetMessages(0)) # type: ignore
        # logger.debug(arcpy.GetMessage)
        print(f"The mmpk for {id_value} already exists.")
    else:
        arcpy.management.CreateMobileMapPackage(map_obj, mmpk_path) # type: ignore
        print(arcpy.GetMessages(0))

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
            print(arcpy.GetMessages(0))
            print(f"The buffer file for {buffer_name} already exists.")
        else:
            buff = create_buffer(point_geom, 100) # type: ignore
            arcpy.CopyFeatures_management(buff, buffer_path)
            print(arcpy.GetMessages(0))
        create_mmpk(aprx_file, buffer_path, dest_folder, id_value) # type: ignore
        print(arcpy.GetMessages(0))

    except arcpy.ExecuteError:
        print(arcpy.GetMessages(0))
    
    except Exception as e:
        print(e)
