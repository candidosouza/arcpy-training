import arcpy

# configura o ambiente de trabalho
arcpy.env.overwriteOutput = True
workspace = arcpy.env.workspace = r"C:\\projects\\arcpy-training"

fc = "C:\\projects\\arcpy-training\\data\\ne_10m_admin_0_countries.shp"

# 1. cria um novo shapefile chamado Countries
# 2. copia as feições do shapefile ne_10m_admin_0_countries.shp para o shapefile Countries
arcpy.management.CopyFeatures("C:\\projects\\arcpy-training\\src\\data\\ne_10m_admin_0_countries.shp", "Countries")

# 1. conta as feições do shapefile ne_10m_admin_0_countries.shp
# 2. imprime o resultado no console
num_feats = arcpy.management.GetCount(fc)
print(f"{fc} has {num_feats} feature(s)")

# 1. cria um novo shapefile chamado India
# 2. copia as feições do shapefile ne_10m_admin_0_countries.shp para o shapefile India
# 3. seleciona as feições do shapefile India onde o atributo NAME é igual a 'India'
result_test = arcpy.analysis.Select(fc, "India",  "NAME = 'India'")
print("result analysis Select", result_test)

# arcpy.GetCount_management(fc) retorna um objeto de resultado que contém informações sobre o número de registros na camada ou tabela especificada.
# result.getOutput(0) é usado para extrair o valor do resultado. O método getOutput(0) é utilizado porque o resultado pode conter várias informações, e o valor desejado geralmente está no índice 0.
# int(result.getOutput(0)) converte o valor extraído para um número inteiro.
result = arcpy.GetCount_management(fc)

# Extraindo o valor do resultado
count = int(result.getOutput(0))

# Imprimindo o resultado
print(f'O número de registros em {fc} é: {count}')
