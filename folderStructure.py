# Créer une structure de dosser à partir d'un dictionnaire 

from pathlib import Path

home = Path.home()
documents = home / "Documents"
 
d = {"Films": [
                "Le seigneur des anneaux",
                "Harry Potter",
                "Moon",
                "Forrest Gump",
            ],
     "Employes": [
        "Paul",
        "Pierre",
        "Marie",
    ],
     "Exercices": [
        "les_variables",
        "les_fichiers",
        "les_boucles",
    ],
}

for parent_dir, child_dir  in d.items():
    for dir in child_dir:
        way_dir = documents / parent_dir / dir
        way_dir.mkdir(exist_ok=True, parents=True)
