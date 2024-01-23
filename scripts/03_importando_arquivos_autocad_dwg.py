import arcpy


# Caminho para o arquivo DWG
# file_dwg = r"C:\\Users\\candido.neto\\Downloads\\espec_geo_modulo_1-3_material\\espec_geo_modulo_1-3_material\\espec_geo_mod_1-3_aula_1_dados\\carta_topografica.dwg"

# Nome da saída no Geodatabase
# out_dataset_name  = "CamadasCAD"
    
# Use a ferramenta CADToGeodatabase para importar o DWG
# o argumento "2004" se refere à versão do formato do Geodatabase para o qual os dados CAD 
# estão sendo convertidos. Nesse caso, "2004" representa a versão disponível no ArcGIS Pro.
# arcpy.CADToGeodatabase_conversion(file_dwg, out_gdb_path, out_dataset_name, "2004")


arcpy.env.workspace = r"C:\\projects\\arcpy-training"

# Definindo as variáveis local
input_cad_dataset = r"C:\\projects\\arcpy-training\\data\\\carta_topografica.dwg"
out_gdb_path = r"C:\\projects\\arcpy-training\\01IntroProject\\01IntroProject.gdb"
out_dataset_name = "analysisresults"
reference_scale = "1000"
# Código EPSG para Sirgas 2000
# sirgas_2000_epsg = 4674
# spatial reference para sirgas 2000
sr_sirgas_2000 = 'GCS_SIRGAS_2000'

# Crie um arquivo geodatabase para o conjunto de dados do recurso
arcpy.management.CreateFileGDB("C:\\projects\\arcpy-training", "01IntroProject.gdb")

# Run CreateFeaturedataset
arcpy.conversion.CADToGeodatabase(input_cad_dataset, out_gdb_path,
                                  out_dataset_name, reference_scale,
                                  sr_sirgas_2000)
