'''Now I'm gonna create a databse named as school and perform some operations on it'''

import mysql.connector as connector

# db = connector.connect(host = "localhost", user = "root", passwd = "root")

# cursor = db.cursor()
# cursor.execute("CREATE DATABASE school")

'I created the databse so now I just need to connect directly to it'

db = connector.connect(host = "localhost", user = "root", password = "root", database = "school")
cursor = db.cursor()

# Creating a table inside the school database

cursor.execute(f'''CREATE TABLE students(
    stId INT NOT NULL PRIMARY KEY,
    stName varchar(20)
    )'''
)

cursor.execute("show tables")

for table in cursor:
    print(table)

