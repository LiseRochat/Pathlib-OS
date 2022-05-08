# L'ordinateur va choisir un nombre entre 1 et 100 et ton objectif est de trouver ce nombre 
import random

number_computer = random.randint(1,100)
number_user = 0
life = 10

while (life != 0) and (number_user != number_computer):

    print("Devinez le nombre mystère")
    number_user = input("Entrez un premier choix :")
    if not number_user.isdigit():
        print("Vous n'avez pas renseigner un nombre valide")
        continue

    if int(number_user) > number_computer:
        print("Le nombre mystère est plus petit")
        life -= 1
        print(f"Il vous reste {life} chance !")
    elif int(number_user)  < number_computer:
        print("Le nombre mystère est plus grand !")
        life -= 1
        print(f"Il vous reste {life} chance !")
    else:
        print("Bravo !!")
        break

print(f"Vous avez epuisé votre quota de chance. Le nombre mystère était {number_computer}")