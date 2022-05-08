print("Calculatrice")
nombre1 = input("Veuillez entrer un premier nombre  : ")
nombre2 = input("Veuillez entrer un deuxième nombre : ")

while (nombre1.isdigit() == False) or (nombre2.isdigit() == False):
    print("Veuillez entrer deux nombres valides")
    nombre1 = input("Veuillez entrer un premier nombre  : ")
    nombre2 = input("Veuillez entrer un deuxième nombre : ")

print(f"Le résultat de l'addition de {nombre1} avec {nombre2} est égal à {int(nombre1) + int(nombre2)}")




