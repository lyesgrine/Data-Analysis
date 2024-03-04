import statistics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, spearmanr
import math

"""    EXO 1    """
"""   Variables Quantitatives    """

"""    1   """

donnees = [12, 15, 18, 20, 22, 25, 30, 35, 40, 45]
moyenne = statistics.mean(donnees)
mediane = statistics.median(donnees)
mode = statistics.mode(donnees)

print(f"Moyenne : {moyenne:.2f}")
print(f"Médiane : {mediane:.2f}")
print(f"Mode : {mode}")



"""   2    """

donnees2 = [10, 12, 15, 18, 20]
ecart_type = math.sqrt(sum((x - statistics.mean(donnees2))**2 for x in donnees2) / len(donnees2))

print(f"Écart type : {ecart_type:.2f}")



"""    3   """

donnees3 = [22, 25, 28, 30, 32, 35, 38, 40, 45]
premier_quartile = np.percentile(donnees3, 25)
deuxieme_quartile = np.percentile(donnees3, 50)
troisieme_quartile = np.percentile(donnees3, 75)

print(f"Premier quartile : {premier_quartile:.2f}")
print(f"Deuxième quartile (médiane) : {deuxieme_quartile:.2f}")
print(f"Troisième quartile : {troisieme_quartile:.2f}")




"""       Variables Qualitatives       """

"""    1   """

donnees_couleurs = ["Rouge", "Bleu", "Vert", "Rouge", "Jaune", "Vert", "Rouge", "Bleu"]
frequence_relative = {couleur: donnees_couleurs.count(couleur) / len(donnees_couleurs) for couleur in set(donnees_couleurs)}

for couleur, freq in frequence_relative.items():
    print(f"{couleur}: {freq:.2f}")



"""   2    """

donnees_genre = ["Homme", "Femme", "Homme", "Femme"]
donnees_couleur_yeux = ["Bleu", "Marron", "Vert", "Bleu"]
tableau_contingence = pd.crosstab(donnees_genre, donnees_couleur_yeux)

print(tableau_contingence)



"""   3    """

donnees_ventes = [25, 15, 30, 20, 10]
labels = ["Rouge", "Bleu", "Vert", "Jaune", "Orange"]

plt.pie(donnees_ventes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("couleur")
plt.axis('equal') 
plt.show()



"""    4    """

mois = ["Janvier", "Février", "Mars", "Avril"]
ventes = [100, 120, 150, 130]

plt.bar(mois, ventes)
plt.xlabel("Mois")
plt.ylabel("Nombre de ventes")
plt.title("mois")
plt.show()




"""  EXO 2   """


"""    1   """

exam_X = np.array([65, 70, 75, 80, 85])
exam_Y = np.array([60, 65, 70, 75, 80])

pearson_corr, _ = pearsonr(exam_X, exam_Y)
print("Pearson correlation coefficient:", pearson_corr)



"""    2   """

age = np.array([25, 30, 35, 40, 45])
income = np.array([50, 60, 70, 80, 90])

slope, intercept = np.polyfit(age, income, 1)
print("Slope:", slope)
print("Intercept:", intercept)



"""    3   """

data = {
    'Gender': ['Homme', 'Homme', 'Homme', 'Femme', 'Femme', 'Femme'],
    'Preference': ['Viande', 'Poisson', 'Légumes', 'Viande', 'Poisson', 'Légumes']
}
df = pd.DataFrame(data)
contingency_table = pd.crosstab(df['Gender'], df['Preference'])
print("Contingency Table:")
print(contingency_table)

chi2, _, _, _ = scipy.stats.chi2_contingency(contingency_table)
contingency_coefficient = np.sqrt(chi2 / (chi2 + len(df)))
print("Contingency Coefficient:", contingency_coefficient)



"""    4   """

weight = np.array([60, 65, 70, 75, 80])
height = np.array([160, 165, 170, 175, 180])


plt.scatter(height, weight)
plt.title('Scatter Plot of Weight vs. Height')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()


"""    5   """

test_X = np.array([70, 75, 80, 85, 90])
test_Y = np.array([60, 65, 70, 75, 80])

spearman_corr, _ = spearmanr(test_X, test_Y)
print("Spearman correlation coefficient:", spearman_corr)
