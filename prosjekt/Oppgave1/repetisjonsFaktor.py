import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv(r'RensetData.csv', sep=",", encoding="latin1")

# Assuming your CSV file has columns 'Total Pieces' and 'Unique Pieces'
df['Repetisjonsfaktor'] = df['Unique_Pieces'] / df['Pieces']

# Lag et horisontalt histogram for å bytte om på x- og y-aksen
plt.figure(figsize=(10, 6))
plt.hist(df['Repetisjonsfaktor'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Forklaringsvariabel 1: Repetisjonsfaktor')
plt.ylabel('Antall LEGO-sett')
plt.xlabel('Repetisjonsfaktor')
plt.grid(axis='x', linestyle='--', alpha=0.5)
#plt.savefig("Repetisjonsfaktor.pdf", format="pdf")
plt.show()

