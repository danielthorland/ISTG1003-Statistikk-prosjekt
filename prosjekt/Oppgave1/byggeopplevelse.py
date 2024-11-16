import pandas as pd
from sklearn.preprocessing import StandardScaler

# Last inn datasettet (juster filstien hvis nødvendig)
file_path = 'RensetData.csv'  # Skriv inn riktig filsti
data = pd.read_csv(file_path)

# Beregn repetisjonsfaktor (Ratio_Unique_Pieces)
data['Ratio_Unique_Pieces'] = data['Unique_Pieces'] / data['Pieces']

# Beregn byggets kompleksitet (Ratio_Pages_Pieces)
data['Ratio_Pages_Pieces'] = data['Pages'] / data['Pieces']

# Standardiser variablene
scaler = StandardScaler()
data[['Z_Ratio_Unique_Pieces', 'Z_Ratio_Pages_Pieces']] = scaler.fit_transform(data[['Ratio_Unique_Pieces', 'Ratio_Pages_Pieces']])

# Konverter kategorisk kompleksitet til numerisk verdi og standardiser
data['Theme_Complexity_Score'] = data['Complexity'].map({'Simple': 1, 'Normal': 2, 'Advanced': 3})
data['Z_Theme_Complexity'] = scaler.fit_transform(data[['Theme_Complexity_Score']])

# Beregn kombinert score
data['Combined_Score'] = (data['Z_Ratio_Unique_Pieces'] + data['Z_Ratio_Pages_Pieces'] + data['Z_Theme_Complexity']) / 3

# Lagre den oppdaterte DataFrame til CSV
data.to_csv('RensetData_Oppdatert.csv', index=False, sep=',', encoding='utf-8')

# Se på resultatene
print(data[['Set_Name', 'Combined_Score']])
