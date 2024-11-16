import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Last inn datasettet (juster filstien hvis nødvendig)
file_path = 'RensetData.csv'
data = pd.read_csv(file_path)

# Beregn forholdet mellom antall sider og totalt antall brikker
data['Ratio_Pages_Pieces'] = data['Pages'] / data['Pieces']

# 2. Histogram av forholdet mellom sider og brikker
plt.figure(figsize=(10, 5))
plt.hist(data['Ratio_Pages_Pieces'], bins=20, color='skyblue', edgecolor='black')
plt.title('Forklaringsvariabel 2: Byggets kompleksitet')
plt.xlabel('Forholdet mellom sider og brikker')
plt.ylabel('Antall LEGO-sett')
#plt.savefig("fVariabel_2.pdf", format="pdf")
plt.show()

