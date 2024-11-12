import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Last inn datasettet (juster filstien hvis nødvendig)
file_path = 'RensetData.csv'  # Skriv inn riktig filsti
data = pd.read_csv(file_path)

# Beregn forholdet mellom antall sider og totalt antall brikker
data['Ratio_Pages_Pieces'] = data['Pages'] / data['Pieces']

# 2. Histogram av forholdet mellom sider og brikker
plt.figure(figsize=(10, 5))
plt.hist(data['Ratio_Pages_Pieces'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram: Fordeling av forholdet mellom sider og brikker')
plt.xlabel('Forholdet mellom sider og brikker')
plt.ylabel('Antall LEGO-sett')
plt.show()

# Sorterte verdier for forholdet mellom sider og brikker
sorted_ratio = data['Ratio_Pages_Pieces'].sort_values()

# Linjeplott med y-aksen som starter fra 0
plt.figure(figsize=(10, 5))
plt.plot(sorted_ratio.values, range(len(sorted_ratio)), marker='o', linestyle='-', markersize=3, color='purple')
plt.title('Linjeplott: Forhold mellom sider og brikker (Y-aksen starter fra 0)')
plt.xlabel('Forholdet mellom sider og brikker')
plt.ylabel('Indeks (sortert)')
plt.show()