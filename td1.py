import statistics
donnees = [12, 15, 18, 20, 22, 25, 30, 35, 40, 45]

moyenne = statistics.mean(donnees)

mediane = statistics.median(donnees)

mode = statistics.mode(donnees)

print(f"Moyenne : {moyenne:.2f}")
print(f"Médiane : {mediane:.2f}")
print(f"Mode : {mode}")

"""       """

import math

donnees2 = [10, 12, 15, 18, 20]

ecart_type = math.sqrt(sum((x - statistics.mean(donnees2))**2 for x in donnees2) / len(donnees2))

print(f"Écart type : {ecart_type:.2f}")


"""       """

import numpy as np

donnees3 = [22, 25, 28, 30, 32, 35, 38, 40, 45]

premier_quartile = np.percentile(donnees3, 25)
deuxieme_quartile = np.percentile(donnees3, 50)
troisieme_quartile = np.percentile(donnees3, 75)

print(f"Premier quartile : {premier_quartile:.2f}")
print(f"Deuxième quartile (médiane) : {deuxieme_quartile:.2f}")
print(f"Troisième quartile : {troisieme_quartile:.2f}")


