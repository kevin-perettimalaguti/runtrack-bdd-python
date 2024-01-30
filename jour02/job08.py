import mysql.connector

"""Creation des tables par le terminal SQL"""

class Zoo:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1478",
        database = "zoo"
        )
        self.cursor = self.mydb.cursor()       

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
    
    def add_cage(self, superficie, capacite_max):
        self.cursor.execute("""
            INSERT INTO cage (superficie, capacite_max)
            VALUES (%s, %s)
        """, (superficie, capacite_max))
        self.mydb.commit()
        
    def modify_cage(self, cage_id, new_superficie, new_capacite_max):
        self.cursor.execute("""
            UPDATE cage
            SET superficie = %s, capacite_max = %s
            WHERE id = %s
        """, (new_superficie, new_capacite_max, cage_id))
        self.mydb.commit()

    def remove_cage(self, cage_id):
        self.cursor.execute("DELETE FROM cage WHERE id = %s", (cage_id,))
        self.mydb.commit()
        
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

    def display_all_animals(self):
        self.cursor.execute("SELECT * FROM animal")
        all_animals = self.cursor.fetchall()
        print("Liste des animaux dans le zoo:")
        for animal in all_animals:
            print(animal)    

    def calculate_total_superficie(self):
        # Calculer la superficie totale de toutes les cages
        self.cursor.execute("SELECT SUM(superficie) FROM cage")
        total_superficie = self.cursor.fetchone()[0]
        print(f"Superficie totale de toutes les cages : {total_superficie} m²")

    def close_connection(self):
        self.mydb.close()

zoo = Zoo()

zoo.add_animal("Tigre", "Félin", 1, "2021-02-26", "Afrique")
zoo.add_animal("Elephant", "Mammifère", 2,"2016-06-18", "Europe")
zoo.add_animal("Panthère Noir", "Félin", 3, "2013-05-17", "Malaisie")
zoo.add_animal("Lion", "Félin", 4, "2011-04-04", "Afrique")
zoo.display_all_animals()

zoo.modify_animal(1, "Tigre à dent de Sabre", "Félin Royal", 1, "2019-07-09", "Amerique du Sud")
zoo.display_all_animals()

zoo.remove_animal(4)
zoo.display_all_animals()

zoo.display_animals_in_cages()

zoo.calculate_total_superficie()

zoo.close_connection()


