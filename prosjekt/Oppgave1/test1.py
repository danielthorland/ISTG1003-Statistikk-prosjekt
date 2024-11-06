import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your CSV file
df = pd.read_csv(r'C:\Users\sondr\gits\ntnu\ISTG1003-Statistikk-prosjekt\prosjekt\Oppgave1\RensetData.csv', sep=",", encoding="latin1")

# Assuming your CSV file has columns 'Total Pieces' and 'Unique Pieces'
df['Repetisjonsfaktor'] = df['Unique_Pieces'] / df['Pieces']

# Lag et horisontalt histogram for å bytte om på x- og y-aksen
#plt.figure(figsize=(10, 6))
#plt.hist(df['Repetisjonsfaktor'], bins=20, orientation='horizontal', color='skyblue', edgecolor='black', alpha=0.7)
#plt.title('Distribusjon av Repetisjonsfaktor for LEGO-sett (Horisontalt)')
#plt.ylabel('Repetisjonsfaktor')
#plt.xlabel('Antall LEGO-sett')
#plt.grid(axis='x', linestyle='--', alpha=0.5)
#plt.show()


# Lag scatter plot for Repetisjonsfaktor vs Pris
plt.figure(figsize=(10, 5))
sns.regplot(x=df['Repetisjonsfaktor'], y=df['Price'], line_kws={"color": "red"}, scatter_kws={"alpha": 0.5})
plt.title('Scatterplot: Forholdet mellom unike brikker og pris')
plt.xlabel('Forholdet mellom unike brikker og totalt antall brikker')
plt.ylabel('Pris (USD)')
plt.show()