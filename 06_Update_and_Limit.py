# import connector
import mysql.connector as connector

# build connection with school database
db = connector.connect(host = "localhost", user = "root", password = "root", database = "school")
cursor = db.cursor() # initialize the cursor

# Update an existing record in database using UPDATE and SET
# Before Update
id = 765
query = f"SELECT stName from students WHERE stId = {id}"

cursor.execute(query)
print("Name Before Update:", cursor.fetchone()[0])

# Updating Record
query = f"UPDATE students SET stName = 'Ubaid Javaid' WHERE stId = {id}"
cursor.execute(query)
db.commit() # to update changes instantly

# After Update
query = f"SELECT stName from students WHERE stId = {id}"

cursor.execute(query)
print("Name Before Update:", cursor.fetchone()[0])

# Limiting the fetch results in order to save memory, using LIMIT
# Suppose, I want to get only 2 records from the query result

print("First 2 records from the result: ")
cursor.execute("SELECT * FROM students LIMIT 2")
for row in cursor.fetchall():
    print(row)
    
# Select only 2 results but don't start from start, instead start after 1st records, using OFFSET

print("2 records by skipping the 1st one from the result: ")
cursor.execute("SELECT * FROM students LIMIT 2 OFFSET 1")
for row in cursor.fetchall():
    print(row)

