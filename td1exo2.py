donnees_couleurs = ["Rouge", "Bleu", "Vert", "Rouge", "Jaune", "Vert", "Rouge", "Bleu"]

frequence_relative = {couleur: donnees_couleurs.count(couleur) / len(donnees_couleurs) for couleur in set(donnees_couleurs)}

for couleur, freq in frequence_relative.items():
    print(f"{couleur}: {freq:.2f}")


"""    """


import pandas as pd

donnees_genre = ["Homme", "Femme", "Homme", "Femme"]
donnees_couleur_yeux = ["Bleu", "Marron", "Vert", "Bleu"]


tableau_contingence = pd.crosstab(donnees_genre, donnees_couleur_yeux)

print(tableau_contingence)

"""    """


import matplotlib.pyplot as plt

donnees_ventes = [25, 15, 30, 20, 10]
labels = ["Rouge", "Bleu", "Vert", "Jaune", "Orange"]

plt.pie(donnees_ventes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("couleur")
plt.axis('equal') 
plt.show()


"""    """


mois = ["Janvier", "Février", "Mars", "Avril"]
ventes = [100, 120, 150, 130]

plt.bar(mois, ventes)
plt.xlabel("Mois")
plt.ylabel("Nombre de ventes")
plt.title("mois")
plt.show()

