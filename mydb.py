import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database connection

cursorObject.execute("CREATE DATABASE elderco")

print ("Conexão com o banco de dados estabelecida!")

