import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Last inn datasettet (juster filstien hvis nødvendig)
file_path = 'RensetData_Oppdatert.csv'  # Skriv inn riktig filsti
data = pd.read_csv(file_path)

# Plot et boxplot for pris per LEGO-tema
plt.figure(figsize=(14, 8))
sns.boxplot(x='Theme', y='Price', data=data, palette='Set3')
plt.title('Prisfordeling per LEGO-tema')
plt.xlabel('LEGO-tema')
plt.ylabel('Pris (USD)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Lagre grafen som en PDF
plt.savefig('Boxplot_Pris_per_LEGO_Tema.pdf', format='pdf')
plt.show()
