import arcpy

def enable_db(db_connection: str, ecp_file: str):
    arcpy.EnableEnterpriseGeodatabase_management(db_connection, ecp_file)


db_path = r"C:\Users\gisuser\Documents\ArcGIS\Projects\vtpk_mmpk_creation\GISDEV.sde"
ecp_file = r"C:\Users\gisuser\Downloads\ArcGISProStandard_ConcurrentUse_1340067.prvs"

enable_db(db_path, ecp_file)