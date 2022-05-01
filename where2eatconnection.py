import mysql.connector
from mysql.connector import Error

# Commands and Queries
command1 = "Find the top 5 restaurants that serve the favorite cuisine of the user\n"
query1 = "SELECT r.name, r.address, r.state FROM restaurant r, rescuisine rc, user u, usercuisine uc, review re WHERE u.userID = 'U1006' AND u.userID = uc.userID AND r.placeID = rc.placeID AND uc.cuisine = rc.cuisine AND r.placeID = re.placeID GROUP BY r.placeID ORDER BY (AVG(re.rating))DESC LIMIT 5;"

command2 = "Find the least-encountered (newer) restaurants for a group based on their preference\n"
query2 = "SELECT r.name, r.address, r.city FROM restaurant r, community c, purchase p, rescuisine rc, groupmembers gm WHERE c.groupID = 1 AND r.placeID = rc.placeID AND rc.cuisine = c.cuisine_overlap AND c.groupID = gm.groupID AND gm.userID = p.userID GROUP BY r.placeID ORDER BY (SELECT COUNT(p.purchaseID)) LIMIT 5;"

command3 = "Find the top 5 closest restaurants that fit the budget for every member in the group\n"
query3 = "SELECT r.name, r.address, r.city FROM restaurant r, Community c WHERE c.groupID = 1 AND c.min_budget >= r.price ORDER BY (POW((r.longitude-c.midLong),2) + POW((r.latitude-c.midLat),2)) LIMIT 5;"

command4 = "Find the 5 most open-minded user in terms of preferred cuisines\n"
query4 = "SELECT u.userID FROM user u, usercuisine uc WHERE u.userID = uc.userID GROUP BY u.userID ORDER BY (COUNT(uc.cuisine))DESC LIMIT 5;"

command5 = "Find the most frivolous user (user that has spent the most money)\n"
query5 = "SELECT u.userID FROM user u, restaurant r, purchase p WHERE u.userID = p.userID AND r.placeID and p.placeID GROUP BY u.userID ORDER BY (SUM(p.cost))DESC LIMIT 1;"

# Method for connecting to database
def get_query(query, command):
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
            print("\nCommand: ", command)
            print("Query: ", query, "\n")

            cursor.execute(query)
            myresult = cursor.fetchall()
            for x in myresult:
                print(x)
            print("\nQuery completed!\n")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed\n")

finished = False
print("\nWelcome to the Where2Eat Database Interface!\n")
while not finished:
    print("\nWhat would you like to do? \nPlease enter any of the values below to specify an action.\n")
    print("1: Submit command 1 - ", command1)
    print("2: Submit command 2 - ", command2)
    print("3: Submit command 3 - ", command3)
    print("4: Submit command 4 - ", command4)
    print("5: Submit command 5 - ", command5)
    print("C: Submit a custom query\n")
    print("E: Exit\n")

    response = input()
    if response == "1":
        get_query(query1, command1)
        print("Would you like to continue? Y/N:")
        exit_response = input()
        if exit_response == "N":
            finished = True
    elif response == "2":
        get_query(query2, command2)
        print("Would you like to continue? Y/N:")
        exit_response = input()
        if exit_response == "N":
            finished = True
    elif response == "3":
        get_query(query3, command3)
        print("Would you like to continue? Y/N:")
        exit_response = input()
        if exit_response == "N":
            finished = True
    elif response == "4":
        get_query(query4, command4)
        print("Would you like to continue? Y/N:")
        exit_response = input()
        if exit_response == "N":
            finished = True
    elif response == "5":
        get_query(query5, command5)
        print("Would you like to continue? Y/N:")
        exit_response = input()
        if exit_response == "N":
            finished = True
    elif response == "C":
        print("\nWhat does your query accomplish? Answer in plain English on one line.\n")
        custom_command = input()
        print("\nVerify that your query adheres to SQL syntax as well as the database schema, and then submit your query below on one line.\n")
        custom_query = input()
        get_query(custom_query, custom_command)
        print("Would you like to continue? Y/N:")
        exit_response = input()
        if exit_response == "N":
            finished = True
    elif response == "E":
        finished = True
    else:
        print("That command is not supported, please try again.\n")
    
    print("\n-------------------------------------------------------")

print("\nYou have chosen to exit the program. Thanks for trying out the Where2Eat database!")
