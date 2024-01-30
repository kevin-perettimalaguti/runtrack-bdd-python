import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1478",
    database = "Laplateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT superficie FROM etage")
superficie = cursor.fetchall()
print(superficie)
result = 0

for i in superficie:
    result += i[0]

print(f"La superficie de La Plateforme est de {result} m2")

