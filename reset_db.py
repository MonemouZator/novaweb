import os
import subprocess

APP_NAME = "nova"
DB_PATH = "db.sqlite3"

def run(cmd):
    print(f"> {cmd}")
    subprocess.run(cmd, shell=True, check=False)

def main():
    print("\n=== Réinitialisation complète de la base de données Django ===\n")

    # Étape 1 : Sauvegarde
    print("Sauvegarde des données actuelles dans dumpdata.json ...")
    run("python manage.py dumpdata > dumpdata.json")

    # Étape 2 : Suppression du fichier SQLite
    if os.path.exists(DB_PATH):
        print(f"Suppression de la base de données : {DB_PATH}")
        os.remove(DB_PATH)

    # Étape 3 : Suppression des migrations
    migrations_path = os.path.join(APP_NAME, "migrations")
    if os.path.exists(migrations_path):
        print(f"Nettoyage des migrations dans {migrations_path} ...")
        for file in os.listdir(migrations_path):
            if file.endswith(".py") and file != "__init__.py":
                os.remove(os.path.join(migrations_path, file))
            elif file.endswith(".pyc"):
                os.remove(os.path.join(migrations_path, file))

    # Étape 4 : Recréation et application des migrations
    print("Recréation des migrations ...")
    run("python manage.py makemigrations")

    print("Application des migrations ...")
    run("python manage.py migrate")

    # Étape 5 : Restauration des données
    print("Restauration des données sauvegardées ...")
    run("python manage.py loaddata dumpdata.json")

    print("\n=== Réinitialisation terminée avec succès ===")

if __name__ == "__main__":
    main()
