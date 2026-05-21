import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

conexion = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

cursor = conexion.cursor()


# INSERT
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
valores = ("veronica", "vero.65@hotmail.com")

cursor.execute(sql, valores)

conexion.commit()

print("Usuario agregado")


# SELECT
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

for users in users:
    print(users)


# UPDATE
sql = "UPDATE users SET name = %s WHERE id = %s"
values = ("Ana", 2)

cursor.execute(sql, values)

conexion.commit()

print("Usuario modificado")


# DELETE 
sql = "DELETE FROM users WHERE id = %s"
values = (6,)

cursor.execute(sql, values)

conexion.commit()

cursor.close()
conexion.close()