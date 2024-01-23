import arcpy

# O código arcpy.env.overwriteOutput = True no arcpy configura a opção de sobrescrever saída. 
#Quando overwriteOutput está definido como True, o ArcGIS permite que os resultados de 
#operações geoprocessamento substituam quaisquer dados existentes com o mesmo nome.
arcpy.env.overwriteOutput = True

# Define o Geodatabase como o diretório de trabalho
# Define o ambiente de trabalho (workspace)
# Agora, todas as operações geoespaciais subsequentes, como criação de feições ou análise espacial,
# serão realizadas dentro desse Geodatabase, a menos que caminhos completos sejam especificados.
workspace = arcpy.env.workspace = r"C:\\projects\\arcpy-training"
out_gdb_path = r"C:\\projects\\arcpy-training\\01IntroProject\\01IntroProject.gdb"
