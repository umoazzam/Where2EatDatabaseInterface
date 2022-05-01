# Where2Eat: Restaurant Database for Solo & Group Dining

Authors: Sohan Bhawtankar, Raunak Bhimsaria, Usman Moazzam

Course: CSDS 341: Introduction to Databases

Professor: Dr. Orhan Ozguner

## Application Background

Indecision amongst friends on where to eat is an age-old adage that plagues most groups in the 21st century. With hundreds of restaurants to choose from, all of varying distances from each person, different cuisine, different rating, and different price, the first-world problem is an easy one to understand. This is an issue that becomes even more difficult the longer a friend group has been in one area, as it's difficult to branch out and find new dining locations once a group of individuals has found a small few that work for everyone in the group to a satisfactory extent.

Despite the complexity of the challenge, bringing together a group of friends at a dining location befitting all of their tastes, budgets and locations becomes easier with the use of a database. The Where2Eat database compiles information about user/group dining profiles, essential information about restaurants, and previous reviews/purchases made. The database also empowers users by allowing them to make queries to find restaurants that best fit their solo tastes as well as their groups' dining preferences. Overall, this system should assist its users and groups in exploring the dining experiences in their area without the risk of restaurants failing to meet their needs, as well as helping them make the essential yet impossible decision: where to eat?

## Data Description (Raunak)

## ER Diagram (Usman)

![Diagram](https://github.com/umoazzam/Where2EatDatabaseInterface/blob/main/Diagrams/where2eatdbER.png)

## Functional Dependencies (Sohan)
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

### Entities (Sohan)

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

### Relations (Raunak)

```
Member_of(user_id, group_id)
PrimaryKey(user_id, group_id)
ForeignKey(user_id) references User.user_id
ForeignKey(group_id) references Groups.group_id
```

This relation keeps track of what users are part of which group. This is a many to many relationship because each group can have multiple users, and each user can be a part of multiple groups.

(RAUNAK) List all other relations and write descriptions for them

## Example Queries (Sohan + Raunak)

## Query 1: Find the top 5 restaurants that serve the favorite cuisine of the user
SELECT r.name, r.address, r.city
FROM restaurant r, rescuisine rc, user u, usercuisine uc, review re
WHERE u.userID = 'U1006' AND u.userID = uc.userID AND r.placeID = rc.placeID AND uc.cuisine = rc.cuisine 
                     AND r.placeID = re.placeID
GROUP BY r.placeID
ORDER BY (AVG(re.rating))DESC LIMIT 5;

## Query 2: Find the least-encountered (newer) restaurants for a group based on their preference
SELECT r.name, r.address, r.city
FROM restaurant r, community c, purchase p, rescuisine rc, groupmembers gm
WHERE c.groupID = 1 AND r.placeID = rc.placeID AND rc.cuisine = c.cuisine_overlap AND c.groupID = gm.groupID AND gm.userID = p.userID
GROUP BY r.placeID
ORDER BY (SELECT COUNT(p.purchaseID)) LIMIT 5;

## Query 3: Find the top 5 closest restaurants that fit the budget for every member in the group
SELECT r.name, r.address, r.city
FROM restaurant r, Community c
WHERE c.groupID = 1 AND c.min_budget >= r.price
ORDER BY (POW((r.longitude-c.midLong),2) + POW((r.latitude-c.midLat),2)) LIMIT 5;

## Query 4: Find the 5 most open-minded user in terms of preferred cuisines
SELECT u.userID
FROM user u, usercuisine uc
WHERE u.userID = uc.userID
GROUP BY u.userID
ORDER BY (COUNT(uc.cuisine))DESC LIMIT 5;

## Query 5: Find the most frivolous user (user that has spent the most money)
SELECT u.userID
FROM user u, restaurant r, purchase p
WHERE u.userID = p.userID AND r.placeID and p.placeID
GROUP BY u.userID
ORDER BY (SUM(p.cost))DESC LIMIT 1;

## Implementation (Usman)

## Team Contributions

### Usman Moazzam

* Project Ideation: ideated project problem and concept, presented to the group for approval
* Project Management: organized/led meetings, managed milestone progress, and set deadlines
* Application Background: wrote/conceived application background section
* ER Diagram: created diagram of general structure of database, ideated all general tables/schema
* SQL Database Server/DB Organization: configured MySQL server and created database using MySQLWorkbench (created all tables/connections)
* Python-MySQL Integration: facilitated connection between Python and MySQL using MySQL Connector
* Python Interaction Script: wrote script to generate queries and send them to the database server
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

* Example SQL Queries
* Python scripts for CSV/Entity generation
* Add more here
