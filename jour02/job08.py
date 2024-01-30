import mysql.connector

class Zoo:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1478",
        database = "zoo"
        )
        self.cursor = self.mydb.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS animal (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255),
                race VARCHAR(255),
                id_cage INT,
                date_naissance DATE,
                pays_origine VARCHAR(255)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cage (
                id INT AUTO_INCREMENT PRIMARY KEY,
                superficie INT,
                capacite_max INT
            )
        """)

    def add_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        self.cursor.execute("""
            INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine)
            VALUES (%s, %s, %s, %s, %s)
        """, (nom, race, id_cage, date_naissance, pays_origine))
        self.mydb.commit()

    def remove_animal(self, animal_id):
        self.cursor.execute("DELETE FROM animal WHERE id = %s", (animal_id,))
        self.mydb.commit()

    def modify_animal(self, animal_id, new_nom, new_race, new_id_cage, new_date_naissance, new_pays_origine):
        self.cursor.execute("""
            UPDATE animal
            SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s
            WHERE id = %s
        """, (new_nom, new_race, new_id_cage, new_date_naissance, new_pays_origine, animal_id))
        self.mydb.commit()

    def display_all_animals(self):
        self.cursor.execute("SELECT * FROM animal")
        all_animals = self.cursor.fetchall()
        print("Liste des animaux dans le zoo:")
        for animal in all_animals:
            print(animal)

    def display_animals_in_cages(self):
        self.cursor.execute("""
            SELECT cage.id, cage.superficie, cage.capacite_max, GROUP_CONCAT(animal.nom SEPARATOR ', ') AS animaux_present
            FROM cage
            LEFT JOIN animal ON cage.id = animal.id_cage
            GROUP BY cage.id
        """)
        animals_in_cages = self.cursor.fetchall()
        print("Liste des animaux dans les cages:")
        for cage in animals_in_cages:
            print(cage)

    def calculate_total_superficie(self):
        self.cursor.execute("SELECT SUM(superficie) FROM cage")
        total_superficie = self.cursor.fetchone()[0]
        print(f"Superficie totale de toutes les cages : {total_superficie} m²")

    def close_connection(self):
        self.mydb.close()

# Exemple d'utilisation de la classe Zoo
zoo = Zoo()

# Ajouter un animal
zoo.add_animal("Lion", "Félin", 1, "2022-01-30", "Afrique")

# Modifier un animal
zoo.modify_animal(1, "Lion Majestueux", "Félin Royal", 1, "2022-01-30", "Afrique du Sud")

# Supprimer un animal
zoo.remove_animal(1)

# Afficher tous les animaux
zoo.display_all_animals()

# Afficher les animaux dans les cages
zoo.display_animals_in_cages()

# Calculer la superficie totale
zoo.calculate_total_superficie()

# Fermer la connexion à la base de données
zoo.close_connection()
