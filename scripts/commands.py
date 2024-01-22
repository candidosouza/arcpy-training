import arcpy


# Se overwriteOutput estiver configurado como True, 
# os resultados da operação serão gravados sobre quaisquer dados existentes com os mesmos nomes de arquivo ou caminho. 
# Se estiver configurado como False (o padrão), a operação falhará se já existirem dados com os mesmos nomes.
arcpy.env.overwriteOutput = True


# Define o Geodatabase como o diretório de trabalho
# Agora, todas as operações geoespaciais subsequentes, como criação de feições ou análise espacial,
# serão realizadas dentro desse Geodatabase, a menos que caminhos completos sejam especificados.
arcpy.env.workspace = r"C:\\projects\\arcpy-training\\01IntroProject\\01IntroProject.gdb"


# 1. cria um novo shapefile chamado Countries
# 2. copia as feições do shapefile ne_10m_admin_0_countries.shp para o shapefile Countries
arcpy.management.CopyFeatures("C:\\projects\\arcpy-training\\src\\data\\ne_10m_admin_0_countries.shp", "Countries")

# 1. conta as feições do shapefile ne_10m_admin_0_countries.shp
# 2. imprime o resultado no console
arcpy.management.GetCount("C:\\projects\\arcpy-training\\src\\data\\ne_10m_admin_0_countries.shp")

# 1. cria um novo shapefile chamado India
# 2. copia as feições do shapefile ne_10m_admin_0_countries.shp para o shapefile India
# 3. seleciona as feições do shapefile India onde o atributo NAME é igual a 'India'
arcpy.analysis.Select("C:\\projects\\arcpy-training\\src\\data\\ne_10m_admin_0_countries.shp", "India",  "NAME = 'India'")



