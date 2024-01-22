import arcpy


database = r"C:\\projects\\arcpy-training\\01IntroProject\\01IntroProject.gdb"
arcpy.env.workspace = database
# arcpy.env.overwriteOutput = True


# fc = feature class
fc = r"C:\\projects\\arcpy-training\\data\\ne_10m_admin_0_countries.shp"

arcpy.analysis.Select(fc, "India",  "NAME = 'India'")

num_feats = arcpy.GetCount_management(fc)

print(f"{fc} has {num_feats} feature(s)")

print("Script Completed")
