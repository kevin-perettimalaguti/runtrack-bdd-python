# Sur mon terminal SQL
"""CREATE TABLE employe(
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> nom VARCHAR(255),
    -> prenom VARCHAR(255),
    -> salaire INT,
    -> id_service INT
    -> );
"""
""" INSERT INTO employe (nom, prenom, salaire, id_service)
    -> VALUES
    ->     ('Madek', 'Lucy', 10000, 10),
    ->     ('Lamorte', 'Vanny', 7500, 11),
    ->     ('Peretti-malaguti', 'Kevin', 25000, 12),
    ->     ('Iribaren', 'Lucas', 8000, 13),
    ->     ('Martini', 'Lucas', 9500, 14);
"""
"""CREATE TABLE service (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> nom VARCHAR(255)
    -> );
"""
"""INSERT INTO service (nom)
    -> VALUES
    ->     ('RH_sapeur_pompier'),
    ->     ('Cuisine'),
    ->     ('PDG'),
    ->     ('Entrainement'),
    ->     ('Direction-Cybersécurite');
"""


"""1ère Partie du Job(sans la class)"""
import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "1478",
#     database = "job07",
# )

# cursor = mydb.cursor()
# request = "SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom AS nom_service " \
#           "FROM employe " \
#           "LEFT JOIN service ON employe.id_service = service.id;"
# cursor.execute(request)
# all_employes = cursor.fetchall()

# print("Tous les employés:")
# for row in all_employes:
#     print(f"{row[0]} | {row[1]} {row[2]} | Salaire: {row[3]} | Service: {row[4]}")
        
# cursor.close()

"""2ère Partie du Job (ajout de la class 'Salarie') en méthode CRUD"""

# Opération CRUD dans la class
class Employe:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1478",
        database = "job07"
        )
        self.request = self.mydb.cursor()
    
    def create_employee(self, nom, prenom, salaire, id_service):
        request = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.request.execute(request, values)
        self.mydb.commit()                       
    
    def read_all_employees(self):
        request = "SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom AS nom_service " \
          "FROM employe " \
          "LEFT JOIN service ON employe.id_service = service.id;"      
        self.request.execute(request)
        all_employes = self.request.fetchall()
        print("Tous les employés:")
        for row in all_employes:
            print(f"{row[0]} | {row[1]} {row[2]} | Salaire: {row[3]} | Service: {row[4]}")        
    
    def update_employee_salary(self, employee_id, new_salary):
        request = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salary, employee_id)
        self.request.execute(request, values)        
        self.mydb.commit()        
        
    def delete_employee(self, employee_id):
        request = "DELETE FROM employe WHERE id = %s"
        values = (employee_id,)
        self.request.execute(request, values)
        self.mydb.commit()
        self.request.close()        
    
    def close_connection(self):
        self.mydb.close()        
        

employees = Employe()

employees.create_employee("Dubois", "Charle", 5000.00, 13)
employees.update_employee_salary(1, 2000.00)
employees.read_all_employees()


employees.close_connection()

        
        
            


        
        
    
    








