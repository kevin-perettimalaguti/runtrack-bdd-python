# Sur le terminal SQL
'''CREATE TABLE etage (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     numero INT,
    ->     superficie INT
    -> );'''
    
'''CREATE TABLE salle(
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> nom VARCHAR(255),
    -> id_etage INT,
    -> capacite INT
    -> );'''