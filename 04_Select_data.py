# import connector
import mysql.connector as connector

# build connection with school database
db = connector.connect(host = "localhost", user = "root", password = "root", database = "school")
cursor = db.cursor() # initialize the cursor

# Select All columns from students table
cursor.execute("SELECT * from students") # to get all cols and rows

rows = cursor.fetchall() # fetch result from last executed query
for row in rows:
    print(row)
print()

# Select Only Name column from students table
cursor.execute("SELECT stName FROM students")

names = cursor.fetchall() # returns a list of tuples
# print("Names Type: ", type(names)) # list

for name in names:
    print(name) # type = tuple
print()

# To fetch only one record we can use fetchone()
cursor.execute("SELECT stName FROM students")
name = cursor.fetchone() # returns a single tuple 
print(name)