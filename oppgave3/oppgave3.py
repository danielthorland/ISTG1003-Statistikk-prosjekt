# importere pakker og funksjoner vi trenger i oppgave 3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # k-gjennomsnitt klyngeanalyse
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib.offsetbox import OffsetImage, AnnotationBbox 

# Leser inn datasettet og ser på de første 5 radene (tallene)

images = pd.read_csv('./oppgave3/mnist_2023.csv', sep = ",", index_col = 0)

images.head()

images = images/255

# Litt informasjon om datasettet ---------------------------------------------------------
print("Bildet har type", type(images))
print("Størrelsen til tabellen er", images.shape)
print("Gjennomsnittsfarge i bilde 50 er", images.iloc[49].mean())
print('Dataformatet til en piksel er', type(images.iloc[1,1]))


# Lag bilder første bildene i datasettet ----------------------------------------
features = np.array(images)
features = features.reshape(features.shape[0], 28,28)

fig = plt.figure(figsize=(10,10))


# -----------------------------------------------------------------------------------------
# Oppgave 3a.1: Hvilke 3 siffer har vi i datasettet? Hvor mange bilder har vi totalt i datasettet?
# -----------------------------------------------------------------------------------------
print("Oppgave 3a.1: Hvilke 3 siffer har vi i datasettet? Hvor mange bilder har vi totalt i datasettet?")

print("\tAntall bilder i datasettet er ", images.shape[0])

print("\tSifferene i datasettet er 9, 3 og 8. Dette ser en enkelt med å se på bildene og se på de første 30 radene i datasettet.")

for i in range(30):
    fig.add_subplot(1, 30, i+1)
    plt.imshow(features[i], cmap = 'gray')
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

plt.show()

# -----------------------------------------------------------------------------------------
# Oppgave 3a.2: Hvilket siffer ligner det 500. bildet i datasettet vårt på? Lag et bilde som viser dette sifferet.
# -----------------------------------------------------------------------------------------
print("Oppgave 3a.2: Hvilke 3 siffer har vi i datasettet? Hvor mange bilder har vi totalt i datasettet?")

plt.imshow(features[499], cmap = 'gray')
plt.show()

print("\tBildet ligner på sifferet 9.")


# ##############################################################################################
# Oppgave 3b.1: Med bruk av K-means klyngeanalyse, finn sentroidene til de tre klyngene.
# -----------------------------------------------------------------------------------------

# Antall klynger
antall_klynger = 3

# Initaliser k-means algoritmen
kmeans = KMeans(n_clusters = antall_klynger, random_state = 1, n_init = 10)

# Tilpass modellen
kmeans.fit(images)

# sentroidene
sentroider = kmeans.cluster_centers_

# Vis sentroidene
fig = plt.figure(figsize=(10,10))
for i in range(antall_klynger):
    fig.add_subplot(1, antall_klynger, i+1)
    plt.imshow(sentroider[i].reshape(28,28), cmap = 'gray')
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

plt.show()

# Oppgave 3b.2: Synes du at grupperingen i klynger er relevant og nyttig? Forklar. Maks 3 setninger.
print("Oppgave 3b.2: Synes du at grupperingen i klynger er relevant og nyttig? Forklar. Maks 3 setninger.")

print("\tJa, grupperingen i klynger er relevant og nyttig. Dette er fordi vi kan se at sentroidene til klyngene er sifferene 3, 8 og 9. Dette er de samme sifrene som vi har i datasettet vårt. Dette betyr at klyngene er relevante og nyttige for å gruppere bildene i datasettet vårt.")


# Oppgave 3b.3: Vi har valgt $K = 3$ for dette eksempelet fordi vi vil finne klynger som representerer de 3 sifrene. Men generelt er $K$ vilkårlig. Kom opp med et forslag for hvordan man (generelt, ikke nødvendigvis her) best kan velge $K$.
print("Oppgave 3b.3: Vi har valgt $K = 3$ for dette eksempelet fordi vi vil finne klynger som representerer de 3 sifrene. Men generelt er $K$ vilkårlig. Kom opp med et forslag for hvordan man (generelt, ikke nødvendigvis her) best kan velge $K$.")
print("\tFor en generell løsning for å finne K kan en bruke albue metoden. Dette er en metode som går ut på å plotte summen av kvadrerte avstander til nærmeste sentroid for hvert K og finne \"kneet\" i grafen der den raskt begynner å flate ut, som gir et godt estimat for K. Alternativt kan en bruke siluett score for å finne en K der alle observasjoner passer bedre til sin egen klynge sammenlignet med andre klynger.")

# Oppgave 3b.4: Kjør analysen igjen med K = 2 og K = 4. Synes du de nye grupperingene er relevante?
print("Oppgave 3b.4: Kjør analysen igjen med K = 2 og K = 4. Synes du de nye grupperingene er relevante?")

K = [2, 4]

for k in K:
    kmeans = KMeans(n_clusters = k, random_state = 1, n_init = 10)
    kmeans.fit(images)
    sentroider = kmeans.cluster_centers_
    fig = plt.figure(figsize=(10,10))
    for i in range(k):
        fig.add_subplot(1, k, i+1)
        plt.imshow(sentroider[i].reshape(28,28), cmap = 'gray')
        plt.xticks([])
        plt.yticks([])
        plt.tight_layout()
    plt.show()

print("\tFor K = 2 ser vi at 3 tallet fortsatt har sin egen klynge, mens 8 og 9 har smeltet sammen til en stor klynge, noe som gjør at denne grupperingen ikke er relevant. For K = 4 ser vi de vanlige tre klyingene, samt en ekstra klynge som har trekt ut en del av 9 tallet, samt en del av 8 tallet. Denne gruppen betyr heller ingenting og gir ikke noen form for ekstra informasjon, kanskje med unntak av at det forteller oss at det er en ganske stor gruppeforskjell mellom siffere som er skrevet rett og skjevt.")

##############################################################################################
# Oppgave 3c: Hierarkisk klyngeanalyse
# -----------------------------------------------------------------------------------------

n_image = 30

sample = images.sample(n = n_image, random_state = 2)

sampleimg = np.array(sample).reshape(sample.shape[0], 28,28)

plt.figure(figsize=(15,10))
ax = plt.subplot()

# Bruk gjennomsnittskobling (method='average')
link = linkage(y = sample, method = 'average', metric = 'euclidean')

dendro = dendrogram(link)

dcoord = np.array(dendro["dcoord"])
icoord = np.array(dendro["icoord"])
leaves = np.array(dendro["leaves"])

idx = np.argsort(dcoord[:, 2])

dcoord = dcoord[idx, :]
icoord = icoord[idx, :]

idx = np.argsort(link[:, :2].ravel())
label_pos = icoord[:, 1:3].ravel()[idx][:n_image]

for i in range(n_image):
    imagebox = OffsetImage(sampleimg[i], cmap = 'gray', interpolation = "bilinear")
    ab = AnnotationBbox(imagebox, (label_pos[i], 0),  box_alignment=(0.5, -0.1), 
                        bboxprops={"edgecolor" : "none"})
    ax.add_artist(ab)

plt.title('Dendrogram for håndskrevne tall')
plt.xlabel('Siffer')
plt.ylabel('Avstand')
plt.xticks([])
plt.show()

# Oppgave 3c.1:  Vurder dendrogrammet nedenfor. Synes du at den hierarkiske grupperingsalgoritmen har laget gode/meningfulle grupper av bildene? (Maks 3 setninger).
print("Oppgave 3c.1:  Vurder dendrogrammet nedenfor. Synes du at den hierarkiske grupperingsalgoritmen har laget gode/meningfulle grupper av bildene? (Maks 3 setninger).")
print("\tNei, dendrogrammet viser liten forskjell mellom grupperingene, slik at om en skulle brukt tre grupper, ville to av gruppene bestått av 3 tall, og den siste ville omfavnet en stor kombinasjon av 3, 8 og 9. Denne inndelingen gir ingen mening og er ikke nyttig for å gruppere bildene i datasettet vårt.")

# Oppgave 3c.2  I koden under har vi brukt gjennomsnittskobling (`method = 'average'`). Hvordan fungerer gjennomsnittskobling?. 
print("Oppgave 3c.2  I koden under har vi brukt gjennomsnittskobling (`method = 'average'`). Hvordan fungerer gjennomsnittskobling?.")
print("\tGjennomsnittskobling fungerer ved å beregne gjennomsnittsavstanden mellom alle punktene i to klynger. Dette betyr at avstanden mellom to klynger er summen av avstandene mellom alle punktene i de to klyngene delt på antall punkter i de to klyngene. Dette gjør at klyngene som blir dannet har en tendens til å være like store og ha en tendens til å være like avstand fra hverandre.")

# Oppgave 3c.3: Velg en annen metode enn 'average' til å koble klyngene sammen (vi har lært om dette i undervisningen, her heter de `single`, `complete` og `centriod`) og lag et nytt dendogram ved å tilpasse koden nedenfor. Ser det bedre/verre ut? (Maks 3 setninger).
print("Oppgave 3c.3: Velg en annen metode enn 'average' til å koble klyngene sammen (vi har lært om dette i undervisningen, her heter de `single`, `complete` og `centriod`) og lag et nytt dendogram ved å tilpasse koden nedenfor. Ser det bedre/verre ut? (Maks 3 setninger).")

plt.figure(figsize=(15,10))
ax = plt.subplot()

# Lag tre forskjellige dendrogrammer med forskjellige metoder

# Single
link = linkage(y = sample, method = 'single', metric = 'euclidean')
dendro = dendrogram(link)
dcoord = np.array(dendro["dcoord"])
icoord = np.array(dendro["icoord"])
leaves = np.array(dendro["leaves"])
idx = np.argsort(dcoord[:, 2])
dcoord = dcoord[idx, :]
icoord = icoord[idx, :]
idx = np.argsort(link[:, :2].ravel())
label_pos = icoord[:, 1:3].ravel()[idx][:n_image]
for i in range(n_image):
    imagebox = OffsetImage(sampleimg[i], cmap = 'gray', interpolation = "bilinear")
    ab = AnnotationBbox(imagebox, (label_pos[i], 0),  box_alignment=(0.5, -0.1), 
                        bboxprops={"edgecolor" : "none"})
    ax.add_artist(ab)

plt.title('Dendrogram for håndskrevne tall med single linkage')
plt.xlabel('Siffer')
plt.ylabel('Avstand')
plt.xticks([])
plt.show()

# Complete
plt.figure(figsize=(15,10))
ax = plt.subplot()
link = linkage(y = sample, method = 'complete', metric = 'euclidean')
dendro = dendrogram(link)
dcoord = np.array(dendro["dcoord"])
icoord = np.array(dendro["icoord"])
leaves = np.array(dendro["leaves"])
idx = np.argsort(dcoord[:, 2])
dcoord = dcoord[idx, :]
icoord = icoord[idx, :]
idx = np.argsort(link[:, :2].ravel())
label_pos = icoord[:, 1:3].ravel()[idx][:n_image]

for i in range(n_image):
    imagebox = OffsetImage(sampleimg[i], cmap = 'gray', interpolation = "bilinear")
    ab = AnnotationBbox(imagebox, (label_pos[i], 0),  box_alignment=(0.5, -0.1), 
                        bboxprops={"edgecolor" : "none"})
    ax.add_artist(ab)

plt.title('Dendrogram for håndskrevne tall med complete linkage')
plt.xlabel('Siffer')
plt.ylabel('Avstand')
plt.xticks([])
plt.show()

# Centroid
plt.figure(figsize=(15,10))
ax = plt.subplot()
link = linkage(y = sample, method = 'centroid', metric = 'euclidean')
dendro = dendrogram(link)
dcoord = np.array(dendro["dcoord"])
icoord = np.array(dendro["icoord"])
leaves = np.array(dendro["leaves"])
idx = np.argsort(dcoord[:, 2])
dcoord = dcoord[idx, :]
icoord = icoord[idx, :]
idx = np.argsort(link[:, :2].ravel())
label_pos = icoord[:, 1:3].ravel()[idx][:n_image]

for i in range(n_image):
    imagebox = OffsetImage(sampleimg[i], cmap = 'gray', interpolation = "bilinear")
    ab = AnnotationBbox(imagebox, (label_pos[i], 0),  box_alignment=(0.5, -0.1), 
                        bboxprops={"edgecolor" : "none"})
    ax.add_artist(ab)

plt.title('Dendrogram for håndskrevne tall med centroid linkage')
plt.xlabel('Siffer')
plt.ylabel('Avstand')
plt.xticks([])
plt.show()

print("\tDendrogrammet med complete style linkage ser best ut av alternativene, men ikke optimalt. Med complete style linkage avstand = 10 vil dendrogrammet vise 8 klynger der netsen alle punktene er i klynge med det riktige sifferet. Dette er ikke optimalt, og har fortsatt en gruppe med blandete siffere, men alt i alt er denne metoden langt bedre enn alternativene.")


##############################################################################################
# Oppgave 3d: Prediksjon
# -----------------------------------------------------------------------------------------

# 3d.1 Hvis vi skulle brukt en metode for å predikere/klassifisere hvilket siffer et håndskrevet tall er, og ikke bare samle dem i klynge, hva ville du brukt?
print("Oppgave 3d.1 Hvis vi skulle brukt en metode for å predikere/klassifisere hvilket siffer et håndskrevet tall er, og ikke bare samle dem i klynge, hva ville du brukt?")

print("\tFor å predikere hvilket siffer det er, ville jeg ha satt opp en klynge analyse med K = 3, og sammenlignet input bildet med sentroidene til klyngene. Så ville jeg ha valgt den klyngen som bildet er nærmest til som prediksjon for hvilket siffer det er.")

# Sett opp en klynge analyse med K = 3 slik som i oppgave 3b.1
kmeans = KMeans(n_clusters = 3, random_state = 1, n_init = 10)
kmeans.fit(images)
sentroider = kmeans.cluster_centers_

