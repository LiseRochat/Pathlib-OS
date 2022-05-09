# ********************************* Sujet ******************************************** Projet de la liste de course avec sauvegarde de la liste dans un fichier JSON, permettant de garder les données entre les différentes utilisations du script Python.

# ************************************** Import MODULE ******************************
# Module me permettant de réaliser différentes oppérations sur mon disque dur comme joindre des chemins ensembles, récupérer créer des dossier 
import os
# Module me permettant de quitter le programme
import sys
# Module me permettant de lire, ecrire, sauvegarder des données au format json
import json

# ************** Chemmin du fichier json **************
CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR,"shoppingList.json")


MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

# ************** Verifie l'existence de la liste **************
if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as file:
        LISTE = json.load(file)
else:
    LISTE = []


while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")

    if user_choice == "1":  # Ajouter un élément
        element = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(element)
        print(f"L'élément {element} a bien été ajouté à la liste.")
    elif user_choice == "2":  # Retirer un élément
        element = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if element in LISTE:
            LISTE.remove(element)
            print(f"L'élément {element} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {element} n'est pas dans la liste.")
    elif user_choice == "3":  # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, element in enumerate(LISTE, 1):
                print(f"{i}. {element}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5":  # Sauvegarder et quitter
        with open(LISTE_PATH, "w") as file:
            json.dump(LISTE, file, indent=4)
        print("À bientôt !")
        sys.exit()
    print("-" * 50)