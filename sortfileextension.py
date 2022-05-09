# Je tri mes fichiers à l'intérieur de mon dossier de téléchargement en fonction de leurs extensions
# Import de la bibliothèque pathlib et de la class Path
from pathlib import Path

# Initialisaton de mon dictionnaire
# extension : dossier
dirs = {
    ".png" : "Images",
    ".jpeg" : "Images",
    ".bmp" : "Images",
    ".webp" : "Images",
    ".gif" : "Vidéos",
    ".mp4" : "Vidéos",
    ".avi" : "Vidéos",
    ".zip" : "Archives",
    ".pdf" : "Documents",
    ".txt" : "Documents",
    ".csv" : "Documents",
    ".xls" : "Documents",
    ".odp" : "Documents",
    ".pages" : "Documents",
    ".mp3" : "Musiques",
    ".wav" : "Musiques",
    ".flac" : "Musiques",
}

# Recupere le chemin vers mon fichier de tri
tri_dir = Path.home() / "Tri"
# Recupère tous les fichiers a l'interieur de mon dossier a l'aide du compréhension de liste
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    # Concatene mon dossier de tri avec le dossier correspondant en fonction de son extension -> Autres si le fichier n'est pas trouvé
    output_dir = tri_dir / dirs.get(f.suffix, "Divers")
    # On créer notre dossier dans lequel on range nos fichiers, on élimine l'erreur si le dossier existe avec exist_ok=True
    output_dir.mkdir(exist_ok=True)
    # On déplace notre fichier d'origine f dans le dossier output f.name : nom de mon fichier
    f.rename(output_dir / f.name)
