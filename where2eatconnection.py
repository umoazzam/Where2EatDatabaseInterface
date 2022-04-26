import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='where2eat',
                                         user='root',
                                         password='MySQLDBPwrd!23')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        print("Sample Query #1: Find the top 5 restaurants that serve " +
              "the favorite cuisine of the user\n")

        query1 = "SELECT name FROM restaurant, user WHERE"
        cursor.execute(query1)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

        print("Sample Query #2: Find the least visited restaurants for " +
              "a group based on their preference\n")

        print("Sample Query #3: Find the top 5 closest restaurants that " +
              "fit the budget for every member in the group\n")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
