import arcpy

def read_sde(sde):
    arcpy.env.workspace = sde # type: ignore
    fcList = arcpy.ListFeatureClasses()
    for fc in fcList: # type: ignore
        print(fc)
sde_path = r"C:\Users\gisuser\Documents\ArcGIS\Projects\vtpk_mmpk_creation\GISDEV.sde"
read_sde(sde_path)