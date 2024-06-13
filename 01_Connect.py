# First install mysql-connector using pip or any other other way
# pip install mysql-connector

# import the connector
import mysql.connector as connector
from mysql.connector import Error
from mysql.connector import errorcode  # to catch any error while connecting to db

"""db = connector.connect(host = "localhost", user = "root", password = "root", database = "dbName")"""
"""if you just want to establish connection with mySql, without specifying the database, then skip the parameter of database"""

db = connector.connect(host="localhost", user="root", password="root")

print(db)  # to check successfull built of connection

"""Now we need a cursor to execute diff db command"""
cursor = db.cursor()

# cursor.execute("<SQL Query>") , cursor will hold the result of query

# cursor.execute("CREATE DATABASE school") # to create a new database
# cursor.execute("DROP DATABASE testPy") # delete/drop a database

cursor.execute("SHOW DATABASES")
for dbs in cursor:
    print(dbs)
print()

"To Catch Error (if there is any) while connecting to the database"

# try:
#     connection = connector.connect(user="testUser", database="test")
# except Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Invalid user name or password !")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist !")
#     else:
#         print(err)
# else:
#     connection.close()

# "Connection Can also be built by giving credentials in the form of dictionary"

# credentials = {
#     "user": "root",
#     "password": "root",
#     "host": "127.0.0.1",  # localhost can also be used
#     "database": "school",
#     "raise_on_warnings": True,  # optional
# }

# connection = connector.connect(
#     **credentials
# )  # ** operator is used against dictionary name to connect

# connection.close()
