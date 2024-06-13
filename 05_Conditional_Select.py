# import connector
import mysql.connector as connector

# build connection with school database
db = connector.connect(host = "localhost", user = "root", password = "root", database = "school")
cursor = db.cursor() # initialize the cursor

'Select Names that end with d'
query = "SELECT stName FROM students WHERE stName LIKE '%d'"
cursor.execute(query)

for row in cursor:
    print(row)

# Like this there can be other conditions on different columns after WHERE clause
id = 789
query = f"SELECT stName from students WHERE stId = {id}"
cursor.execute(query)
name = cursor.fetchone() # tuple with one value

print(f"Student with id {id}:", name[0])    