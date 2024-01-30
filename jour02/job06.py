import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1478",
    database = "Laplateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT capacite FROM salle")
capacite = cursor.fetchall()
result = 0

for i in capacite:
    result += i[0]
    
print(f"La capcacité de toutes les salles est de : {result}")

cursor.close()
mydb.close()