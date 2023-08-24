import arcpy

aprx = arcpy.mp.ArcGISProject("blank.aprx")
aprx.saveACopy("newaprx.aprx")