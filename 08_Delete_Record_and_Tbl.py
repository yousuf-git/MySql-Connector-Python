# import connector
import mysql.connector as connector

# build connection with school database
db = connector.connect(host = "localhost", user = "root", password = "root", database = "school")
cursor = db.cursor() # initialize the cursor

# Creating a test table that I can delete and test the delete command
# query = "CREATE TABLE test(col1 INT PRIMARY KEY, col2 INT)" # once executed this then comment it
# cursor.execute(query)
# db.commit()

# query = "SHOW TABLES"
# cursor.execute(query)

# print("Tables list:")
# for tbl in cursor.fetchall():
#     print(tbl, end= " ")

# # Drop the table "test"
# query = "DROP TABLE test"
# cursor.execute(query)
# db.commit()

# query = "SHOW TABLES"
# cursor.execute(query)

# print("\nTables list After deletion:")
# for tbl in cursor.fetchall():
#     print(tbl, end= " ")

# Now I want to remove the record of student with stId 791, which is muneeb

# First check student Name before deletion
cursor.execute("SELECT stName from students where stId = 791")
print("Student with student Id 791:", cursor.fetchone()[0])

# delete the record of student
cursor.execute("DELETE from students where stId = 791")
db.commit()

# Now again try to check the name of same student
cursor.execute("SELECT stName from students where stId = 791")
if not cursor.fetchone():
    print("No Student Found")
else:
    print("Student with student Id 791:", cursor.fetchone()[0])

print()