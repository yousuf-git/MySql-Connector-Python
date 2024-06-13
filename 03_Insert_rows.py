# import connector
import mysql.connector as connector

# build connection with school database
db = connector.connect(host = "localhost", user = "root", password = "root", database = "school")

cursor = db.cursor()

# Insert a single row inside the students table

query = ("INSERT INTO students (stId, stName) VALUES (%s, %s)")
row = (789, "Yousuf")

# cursor.execute(query, row)

db.commit() # to update the changes in databse

# Insert Multiple rows at once, query will be same
rows = [
    (765, "Ubaid"),
    (795, "Hammad"), 
    (791, "Muneeb"),
    ]

cursor.executemany(query, rows)
db.commit()