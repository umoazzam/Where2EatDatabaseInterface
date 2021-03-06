# Where2Eat: Restaurant Database for Solo & Group Dining

Authors: Sohan Bhawtankar, Raunak Bhimsaria, Usman Moazzam

Course: CSDS 341: Introduction to Databases

Professor: Dr. Orhan Ozguner

## Application Background

Indecision amongst friends on where to eat is an age-old adage that plagues most groups in the 21st century. With hundreds of restaurants to choose from, all of varying distances from each person, different cuisine, different rating, and different price, the first-world problem is an easy one to understand. This is an issue that becomes even more difficult the longer a friend group has been in one area, as it's difficult to branch out and find new dining locations once a group of individuals has found a small few that work for everyone in the group to a satisfactory extent.

Despite the complexity of the challenge, bringing together a group of friends at a dining location befitting all of their tastes, budgets and locations becomes easier with the use of a database. The Where2Eat database compiles information about user/group dining profiles, essential information about restaurants, and previous reviews/purchases made. The database also empowers users by allowing them to make queries to find restaurants that best fit their solo tastes as well as their groups' dining preferences. Overall, this system should assist its users and groups in exploring the dining experiences in their area without the risk of restaurants failing to meet their needs, as well as helping them make the essential yet impossible decision: where to eat?

## Data Description

We got our data from the Univeristy of California Irvine Machine-Learning repository which we found on [Kaggle](https://www.kaggle.com/datasets/uciml/restaurant-data-with-consumer-ratings?select=rating_final.csv). The repository got its data from the National Centre for Research and Technological Development CENIDET.

We wrote python scripts that we ran on the raw data to get the desired data that could be put in our database. For example, we randomly generated the purchase history for each user and randomly created groups from the user data set (for which we had to then calculate the type (family, friends, or undecided), the minimum budget, and the cuisine overlap for each group).

Our data consists for several csv files namely:

* groupMembers: Contains the userID of the members of all the groups.
* groups: Contains the type (family, friends, or undecided), the minimum budget, the cuisine overlap, and the mean location for all the groups.
* purchases: Contains which user spent how much at which restaurant.
* resCuisine: Contains the cuisines that the restaurant offers.
* restaurants: Contains the location (longitide and latitude), name, address, city, state, what type of alcohol they serve (and whether they don't), smoking restrictions, dress code, accessibilty, price level, ambience, and the type of area (closed or open) of the restaurants.
* reviews: Contains the reviews - overall rating, food rating, and service rating - of the restaurants by the users.
* userCuisine: Contains the preferred cuisines of the users
* users: Contains the location (longitude and latitude), whether they smoke, the drink level, the dress preference, the ambeince preference, the transportation, the marital status, the birth year, the activity (student, professional, or unemployed), the weight, the budget, and the height of the users.

## ER Diagram

![Diagram](https://github.com/umoazzam/Where2EatDatabaseInterface/blob/main/Diagrams/where2eatdbER.png)

## Functional Dependencies
```
User:\
userID -> latitude, longitude, smoker, drink_level, dress_preference, ambience, transport, marital_status, birth_year, activity, weight, budget, height

latitude, longitude -> userID
```
```
Community:\
groupID -> type, min_budget, cuisine_overlap, midLong, midLat
```
```
Restaurant:\
placeID -> latitude, longitude, name, address, city, state, alcohol, smoking_area, dress_code, accessibility, price, Rambience, area

latitude, longitude -> placeID

name, address -> placeID
```

```
Purchase:\
purchaseID -> userID, placeID, cost
```
```
Review:\
reviewID -> userID, placeID, rating, food_rating, service_rating

userID, placeID -> reviewID
```

## Schemas

### Entities

#### User
```
User (
  `userID`: char(30),
  `latitude: double,
  `longitude`: double,
  `smoker`: char(30),
  `drink_level`: char(30),
  `dress_preference`: char(30),
  `ambience`: char(30),
  `transport`: char(30),
  `marital_status`: char(30),
  `birth_year`: int,
  `activity`: char(30),
  `weight`: int,
  `budget`: int,
  `height`: double
)
```

This table holds information about every user. Each tuple will contain a unique user and various characteristics associated with them.

#### Community

```
Community (
  `groupID`: int,
  `type`: char(30),
  `min_budget`: int,
  `cuisine_overlap`: char(30),
  `midLong`: double,
  `midLat`: double
)
```

This table holds information about groups, which consist of multiple people. Each group is unique and has certain characteristics associated with it. These include budget constraints, type of group (family, relationship, work friends), and favorite cuisines.

#### Restaurant

```
Restaurant (
  `placeID`: int,
  `latitude`: double,
  `longitude`: double,
  `name`: char(100),
  `address`: char(100) ,
  `city`: char(30),
  `state`: char(30),
  `alcohol`: char(30),
  `smoking_area`: char(30),
  `dress_code`: char(30),
  `accessibility`: char(30),
  `price`: int,
  `Rambience`: char(30),
  `area`: char(30)
```

This table stores information about every unique restaurant identified by their placeID. 


#### Purchase

```
Purchase (
  `userID: char(30), 
  `placeID`: INT, 
  `purchaseID`: INT, 
  `cost`: INT
)
ForeignKey(userID) references User.userID
ForeignKey(placeID) references Restaurant.placeID
```
This weak entity stores the purchase history at restaurants of every user. 

#### Review

```
Review (
  `userID`: char(30), 
  `placeID`: INT, 
  `reviewID`: INT, 
  `rating`: INT,
  `food_rating`: INT,
  `service_rating`: INT
)
ForeignKey(userID) references User.userID
ForeignKey(placeID) references Restaurant.placeID
```

This table stores reviews of a user. Every user may have multiple reviews of different restaurants. These reviews include the date they were written, rating, and a written section for a specific review. 

#### UserCuisine

```
`UserCuisine` (
  `userID`: char(30),
  `cuisine`: char(30)
)
ForeignKey(userID) references User.userID
```

This weak entity stores each cuisine a user prefers to eat. 

#### ResCuisine

```
`ResCuisine` (
  `placeID`: int,
  `cuisine`: char(30)
)
ForeignKey(placeID) references Restaurant.placeID
```

This weak entity stores every cuisine a restaurant serves.

#### GroupMembers

```
`GroupMembers` (
  `groupID`: int,
  `userID`: char(30)
)
ForeignKey(userID) references User.userID
ForeignKey(groupID) references Community.groupID
```

This weak entity stores every member inside a group/community. 

### Relations

```
Member_of(user_id, group_id)
PrimaryKey(user_id, group_id)
ForeignKey(user_id) references User.user_id
ForeignKey(group_id) references Groups.group_id
```

This relation keeps track of what users are part of which group. This is a many to many relationship because each group can have multiple users, and each user can be a part of multiple groups.

All of our other relations are weak relations and thus have not been listed here to prevent any redundancy.


## Example Queries

5 out of our 6 queries could not be translated into RA and TRC due to the incompatibility of those formats with aggregate functions.
Our 6th query is written in all formats - SQL, RA, TRC.

### Query 1: Find the top 5 restaurants that serve the favorite cuisine of the user
#### SQL
```
SELECT r.name, r.address, r.city
FROM restaurant r, rescuisine rc, user u, usercuisine uc, review re
WHERE u.userID = 'U1006' AND u.userID = uc.userID AND r.placeID = rc.placeID AND uc.cuisine = rc.cuisine 
                     AND r.placeID = re.placeID
GROUP BY r.placeID
ORDER BY (AVG(re.rating))DESC LIMIT 5;
```

### Query 2: Find the least-encountered (newer) restaurants for a group based on their preference
#### SQL
```
SELECT r.name, r.address, r.city
FROM restaurant r, community c, purchase p, rescuisine rc, groupmembers gm
WHERE c.groupID = 1 AND r.placeID = rc.placeID AND rc.cuisine = c.cuisine_overlap AND c.groupID = gm.groupID AND gm.userID = p.userID
GROUP BY r.placeID
ORDER BY (SELECT COUNT(p.purchaseID)) LIMIT 5;
```

### Query 3: Find the top 5 closest restaurants that fit the budget for every member in the group
#### SQL
```
SELECT r.name, r.address, r.city
FROM restaurant r, Community c
WHERE c.groupID = 1 AND c.min_budget >= r.price
ORDER BY (POW((r.longitude-c.midLong),2) + POW((r.latitude-c.midLat),2)) LIMIT 5;
```
### Query 4: Find the 5 most open-minded user in terms of preferred cuisines
#### SQL
```
SELECT u.userID
FROM user u, usercuisine uc
WHERE u.userID = uc.userID
GROUP BY u.userID
ORDER BY (COUNT(uc.cuisine))DESC LIMIT 5;
```

### Query 5: Find the most frivolous user (user that has spent the most money)
#### SQL
```
SELECT u.userID
FROM user u, restaurant r, purchase p
WHERE u.userID = p.userID AND r.placeID = p.placeID
GROUP BY u.userID
ORDER BY (SUM(p.cost))DESC LIMIT 1;
```

### Query 6: Find all the restaurants that serve wine, are wheelchair accessible, have a low price budget, and have an informal dress-code
#### SQL
```
SELECT r.name
FROM restaurant r
WHERE r.price = 1 AND r.dress_code = "informal" AND r.alcohol = "Wine-Beer" AND r.accessibility = "completely"
```

#### TRC
```
{t|(???r) (r ??? restaurant) (t[name] = r[name] ??? r[price] = 1 ??? r[dress_code] = "informal" ??? r[alcohol] = "Wine-Beer" ??? r[accessibility] = "completely"}
```
#### RA
```
??_name(??_(price=1???dress_code ="informal"???alcohol="Wine-Beer"???accessibility="completely") (restaurant))
```

## Implementation

### Database/Server

This database and its corresponding ER diagram were generated using MySQLWorkbench and hosted on a MySQL server on a device running MacOS Monterey. The files for the server/DB can be found in the *Server and Database* directory. 

### User Interface

The user interface for the database was created using a Python script titled *where2eatconnection.py*. This interface is a tool with which the user can connect with the database and send queries about its contents. This includes choosing from the 5 sample queries listed above and receiving the appropriate response or entering in a valid SQL query of their own. Overall, the user interface empowers the user to seek information about other users, groups and restaurants as well as which restaurants best correlate with users??? solo and group dining preferences. The output from the demonstration of this tool can be found in the *Output* directory in both text and png format.

## Team Contributions

### Usman Moazzam

* Project Ideation: ideated project problem and concept, presented to the group for approval
* Project Management: organized/led meetings, managed milestone progress, and set deadlines
* Application Background: wrote/conceived application background section
* ER Diagram: created diagram of general structure of database, ideated all general tables/schema
* SQL Database Server/DB Organization: configured MySQL server and created database using MySQLWorkbench (created all tables/connections)
* Python-MySQL Integration: facilitated connection between Python and MySQL using MySQL Connector
* Python Interaction Script: wrote script for user interaction to generate queries and send them to the database server
* Demo: organized demonstration to TAs for review

### Sohan Bhawtanker

* Example SQL Queries
* Example Relational Algebra Queries
* Python scripts for CSV/Entity generation
  * Randomized purchase history for each user
  * Calculated locations of groups
  * Generated extra tables to prevent lists
  * Fixed formatting to allow for quick insertion into SQL
* Writing Schemas
* Writing Functional Dependencies

### Raunak Bhimsaria

* Example SQL Queries.
* Python scripts for CSV/Entity generation:
  * Generated random groups from the user dataset.
  * Calculated the type (family, friends, or undecided), the minimum budget, and the cuisine overlap for the groups.
  * Removed unwanted columns from the user and restaurant data set.
  * Merged csv files to facilitate moving data into database.
* Writing the Relational Algebra and Tuple Relational Calculus.
* Writing the Data Description.

## What we learned

This was the first time any of us have endeavored to create a database project this large, so this assignment posed an extremely valuable learning experience for us. Throughout the semester working on the project, we got the opportunity to expand on our project management/development skills, communication skills, and presentation skills. We also learned a lot about database management and generation and how it differs in application from what we learn about databases conceptually. An example of this was how list variables in csvs can be expressed; we originally believed there was some list type that could be used to store a list in a specific varibale for each observation, but found while creating the database that no such type existed. This meant we had to add in new entity tables to attach entities to corresponding list variables, which is where our usercuisines, rescuisines, and groupmembers tables came from. Overall, this assignment was extremely valuable for us as it gave us the chance to apply our databases knowledge and develop a cool academic project which would have use in real applications.
