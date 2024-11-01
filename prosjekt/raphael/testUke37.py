import statistics as stats

import pandas as pd # lese data fra csv-fil og bruke DataFrames
import seaborn as sns # plotting
#sns.set(style = 'whitegrid', font_scale = 1.5) # utseende av plott
import matplotlib.pyplot as plt # mer plotting
import numpy as np # matematikk
import statsmodels.api as sms # regresjonen
import statsmodels.formula.api as smf # formel for regresjonen


df = pd.read_csv('./skostr_hoyde.csv')
df.shape # dimenensjonen til datasettet

# Merk at en del kolonnenavn inneholder punktum
# Dette er generelt uheldig når vi programmerer, så vi 
# erstatter alle punktum med underscore

df.columns = df.columns.str.replace(".", "_")

df.head() # ser på de 5 første linjene i datasettet

# Vi lager oss en funksjon som koder fra timer:minutter:sekunder til minutter
def get_min(time_str):
    h, m, s = time_str.split(':')
    return round(int(h)*60 + int(m) + int(s)/60 , 2)

# Lager en TimeMin kolonne i datasettet
df['TimeMin'] = df['Time'].apply(get_min)

# Plotter tid mot distanse for å få et inntrykk av datasettet
sns.relplot(x='Distance', y='TimeMin',data = df)
plt.xlim(0,10); plt.ylim(0,60)
plt.ylabel('Tid [min]'); plt.xlabel('Distanse [km]')
plt.show()