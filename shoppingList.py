# Programme en ligne de commande qui vas permettre de gérer une liste de course
shopping_list = []
user_action = 0

while user_action != 5:

    print("""
        Choisissez parmi les 5 options suivantes : 
        1: Ajouter un élément à la liste
        2: Retirer un élément de la liste
        3: Afficher la liste
        4: Vider la liste
        5: Quitter
    """)
    user_action = input("Votre choix : ")
    if not(user_action.isdigit() and 1 <= int(user_action) <= 5):
        print("Choix inconnus")
        continue
    if user_action == "1":
        element = input("Entrez le nom d'un élément à ajouter à la liste de course : ")
        if element.isdigit() == False:
            shopping_list.append(element)
            print(f"L'element : {element} à bien été ajouté à la liste de course")
        else: 
            print("Veuillez renseigner un élément valide.")

    elif user_action == "2":
        element = input("Entrez le nom de l'élément à supprimer à la liste de course : ")
        if element in shopping_list:
            shopping_list.remove(element)
            print(f"L'element {element} à été supprimé de la liste de course")
        else:
            print(f"L'element : {element} n'est pas présent dans la liste")

    elif user_action == "3":
        if len(shopping_list) == 0:
            print("Votre Liste est vide !")
        else: 
            print("Votre liste de course : ")
            for i in shopping_list:
                print(i)

    elif user_action == "4":
        if shopping_list:
            shopping_list.clear()
            print("Votre liste de course à été vidé : ")
        else:
            print("Votre liste de course est vide")

    else:
        print("A Bientot !")
        break
    
