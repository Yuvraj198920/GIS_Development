import arcpy

gdb_dir = r"C:\Users\gisuser\Documents\ArcGIS\Packages\Introducing_ArcGIS_Pro_7f7355\sample_gdb.gdb"
desc = arcpy.ListFeatureClasses(gdb_dir)
print(desc)
print(arcpy.GetMessage(0))

message_count = arcpy.GetMessageCount()
print(message_count)