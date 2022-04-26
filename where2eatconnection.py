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

        print("\nSample Query #1: Find the top 5 restaurants that serve the favorite cuisine of the user\n")

        query1 = "SELECT r.name, r.address, r.state FROM restaurant r, rescuisine rc, user u, usercuisine uc, review re WHERE u.userID = 'U1006' AND u.userID = uc.userID AND r.placeID = rc.placeID AND uc.cuisine = rc.cuisine AND r.placeID = re.placeID GROUP BY r.placeID ORDER BY (AVG(re.rating))DESC LIMIT 5;"

        print("\nSample Query #2: Find the least-encountered (newer) restaurants for a group based on their preference\n")

        query2 = "SELECT r.name, r.address, r.city FROM restaurant r, community c, purchase p, rescuisine rc, groupmembers gm WHERE c.groupID = 1 AND r.placeID = rc.placeID AND rc.cuisine = c.cuisine_overlap AND c.groupID = gm.groupID AND gm.userID = p.userID GROUP BY r.placeID ORDER BY (SELECT COUNT(p.purchaseID)) LIMIT 5;"

        print("\nSample Query #3: Find the top 5 closest restaurants that fit the budget for every member in the group\n")

        query3 = "SELECT r.name, r.address, r.city FROM restaurant r, Community c WHERE c.groupID = 1 AND c.min_budget >= r.price ORDER BY (POW((r.longitude-c.midLong),2) + POW((r.latitude-c.midLat),2)) LIMIT 5;"

        print("\nSample Query #4: Find the 5 most open-minded user in terms of preferred cuisines\n")

        query4 = "SELECT u.userID FROM user u, usercuisine uc WHERE u.userID = uc.userID GROUP BY u.userID ORDER BY (COUNT(uc.cuisine))DESC LIMIT 5;"

        print("\nSample Query #5: Find the most frivolous user (user that has spent the most money)\n")

        query5 = "SELECT u.userID FROM user u, restaurant r, purchase p WHERE u.userID = p.userID AND r.placeID and p.placeID GROUP BY u.userID ORDER BY (SUM(p.cost))DESC LIMIT 1;"

        cursor.execute(query5)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
