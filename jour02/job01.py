import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1478",
    database = "Laplateforme",
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM etudiants")
results = cursor.fetchall()

print(results)

cursor.close()
mydb.close()

