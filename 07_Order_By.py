# import connector
import mysql.connector as connector

# build connection with school database
db = connector.connect(host = "localhost", user = "root", password = "root", database = "school")
cursor = db.cursor() # initialize the cursor

# You can sort the result of query in ascending or descending order, based on a specific column

query = "SELECT * FROM students ORDER BY marks DESC" # if DESC is not written, by default it is in ascending
cursor.execute(query)

for row in cursor.fetchall():
    print(row)