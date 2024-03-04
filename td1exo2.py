import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, spearmanr



donnees_couleurs = ["Rouge", "Bleu", "Vert", "Rouge", "Jaune", "Vert", "Rouge", "Bleu"]

frequence_relative = {couleur: donnees_couleurs.count(couleur) / len(donnees_couleurs) for couleur in set(donnees_couleurs)}

for couleur, freq in frequence_relative.items():
    print(f"{couleur}: {freq:.2f}")


"""    """



donnees_genre = ["Homme", "Femme", "Homme", "Femme"]
donnees_couleur_yeux = ["Bleu", "Marron", "Vert", "Bleu"]


tableau_contingence = pd.crosstab(donnees_genre, donnees_couleur_yeux)

print(tableau_contingence)

"""    """



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


"""          """



# Exercice 2: Correlation
# Scores for two exams
exam_X = np.array([65, 70, 75, 80, 85])
exam_Y = np.array([60, 65, 70, 75, 80])

# Calculate Pearson correlation coefficient
pearson_corr, _ = pearsonr(exam_X, exam_Y)
print("Pearson correlation coefficient:", pearson_corr)

# Exercice 2: Linear regression
# Monthly income in thousands of Dinars based on age
age = np.array([25, 30, 35, 40, 45])
income = np.array([50, 60, 70, 80, 90])

# Perform linear regression
slope, intercept = np.polyfit(age, income, 1)
print("Slope:", slope)
print("Intercept:", intercept)

# Exercice 2: Contingency table
# Food preference based on gender
data = {
    'Gender': ['Homme', 'Homme', 'Homme', 'Femme', 'Femme', 'Femme'],
    'Preference': ['Viande', 'Poisson', 'Légumes', 'Viande', 'Poisson', 'Légumes']
}
df = pd.DataFrame(data)

contingency_table = pd.crosstab(df['Gender'], df['Preference'])
print("Contingency Table:")
print(contingency_table)

# Calculate contingency coefficient
chi2, _, _, _ = scipy.stats.chi2_contingency(contingency_table)
contingency_coefficient = np.sqrt(chi2 / (chi2 + len(df)))
print("Contingency Coefficient:", contingency_coefficient)

# Exercice 2: Scatter plot
# Weight and height data
weight = np.array([60, 65, 70, 75, 80])
height = np.array([160, 165, 170, 175, 180])

# Scatter plot
plt.scatter(height, weight)
plt.title('Scatter Plot of Weight vs. Height')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()

# Exercice 2: Spearman correlation coefficient
# Scores for two tests
test_X = np.array([70, 75, 80, 85, 90])
test_Y = np.array([60, 65, 70, 75, 80])

# Calculate Spearman correlation coefficient
spearman_corr, _ = spearmanr(test_X, test_Y)
print("Spearman correlation coefficient:", spearman_corr)
