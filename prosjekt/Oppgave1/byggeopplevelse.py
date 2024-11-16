import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Last inn datasettet (juster filstien hvis nødvendig)
file_path = 'RensetData.csv'  # Skriv inn riktig filsti
data = pd.read_csv(file_path)

# Beregn repetisjonsfaktor (Ratio_Unique_Pieces)
data['Ratio_Unique_Pieces'] = data['Unique_Pieces'] / data['Pieces']

# Beregn byggets kompleksitet (Ratio_Pages_Pieces)
data['Ratio_Pages_Pieces'] = data['Pages'] / data['Pieces']

# Konverter kompleksitet basert på tema til numeriske verdier
data['Theme_Complexity_Score'] = data['Complexity'].map({'enkle': 1, 'normale': 2, 'avanserte': 3})

# Beregn kombinert score som en enkel sum eller gjennomsnitt av de tre variablene
data['Combined_Score'] = (data['Ratio_Unique_Pieces'] + data['Ratio_Pages_Pieces'] + data['Theme_Complexity_Score']) / 3

# Lagre den oppdaterte DataFrame med den nye kolonnen tilbake til CSV
data.to_csv('RensetData_Oppdatert.csv', index=False, sep=',', encoding='utf-8')

# Plot scatterplot mellom kombinert score og pris med regresjonslinje
plt.figure(figsize=(10, 6))
sns.regplot(x='Combined_Score', y='Price', data=data, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Sammenheng mellom Byggeopplevelse og Pris')
plt.xlabel('Kombinert Score for Byggeopplevelse')
plt.ylabel('Pris (USD)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('Scatterplot_Byggeopplevelse_vs_Pris.pdf', format='pdf')
plt.show()