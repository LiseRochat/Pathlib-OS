# Le but de ce projet est de lire un fichier et tous les noms qu'il contient, trier cette liste de noms, et ré-écrire la liste dans l'ordre alphabétique.

# 1. Ouvrir le fichier name.txt et lire sont contenu 
import os

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR,"name.txt")

if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as file:
        lists = file.read().splitlines()
    print(lists)
else:
    print("Le fichier n'existe pas !")
# 2. Récuperer chaque prénom séparément dans une liste
names = []
for list in lists:
    names.extend(list.split())
# 3. Nettoyer les prénoms pour enlever les virgules, points ou espace
name_finaly = [name.strip(",. ") for name in names]
# 4. Ecrire la liste ordonnée et nettoyée dans un nouveau fichier texte
LISTE_ORDER_PATH =  os.path.join(CUR_DIR,"nameOrder.txt")
with open(LISTE_ORDER_PATH, "w") as f:
    f.write("\n".join(sorted(name_finaly)))