import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'RensetData.csv', sep=",", encoding="latin1")

# Calculate the Repetisjonsfaktor
df['Repetisjonsfaktor'] = df['Unique_Pieces'] / df['Pieces']


# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df['Pieces'], df['Unique_Pieces'], color='skyblue', edgecolor='black')
plt.xlabel('Antall Brikker')
plt.ylabel('Antall Unike Brikker')
plt.title('Antall Unike Brikker vs Antall Brikker for LEGO Set')
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.tight_layout()  # Adjust layout for readability
plt.show()

