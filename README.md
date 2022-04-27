# Where2Eat: Restaurant Database for Group Dining

Authors: Sohan Bhawtankar, Raunak Bhimsaria, Usman Moazzam

Course: CSDS 341: Introduction to Databases

Professor: Dr. Orhan Ozguner

## Application Background

Indecision amongst friends on where to eat is an age-old adage that plagues most groups in the 21st century. With hundreds of restaurants to choose from, all of varying distances from each person, different cuisine, different rating, and different price, the first-world problem is an easy one to understand. This is an issue that becomes even more difficult the longer a friend group has been in one area, as it's difficult to branch out and find new dining locations once a group of individuals has found a small few that work for everyone in the group to a satisfactory extent.

Despite the complexity of the challenge, bringing together a group of friends at a dining location befitting all of their tastes, budgets and locations becomes easier with the use of a database. Where2Eat utilizes a database to allow users to organize their dining profiles, compare dining experiences with individuals in their constructed groups (work, family, friends, other social groups), and then receive a list of restaurants for them to try based on their collective wants and needs in a dining location. Overall, this system should assist its users and groups in exploring the dining experiences in their area without the risk of restaurants failing to meet their needs, as well as helping them make the essential yet impossible decision: where to eat?

## Data Description (Raunak)

## ER Diagram (Usman)

## Functional Dependencies (Sohan)

## Schemas

### Entities (Sohan)

```
User(user_id: INT, name: CHAR, age: INT, neighborhood: CHAR, phone_num: CHAR, fave_foods{CHAR}: CHAR, cuisines{CHAR}: CHAR, budget: INT, drink_lvl: CHAR, curiosity: INT)
```

This table holds information about every user. Each tuple will contain a unique user and various characteristics associated with them.

```
Groups(group_id: INT, members{INT}: INT, fave_food_overlap: CHAR, cuisine_overlap: CHAR, type: CHAR, min_budget: INT, midpoint: INT)
```

This table holds information about groups, which consist of multiple people. Each group is unique and has certain characteristics associated with it. These include budget constraints, type of group (family, relationship, work friends), and favorite cuisines.

```
Restaurant(restaurant_id: INT, budget: INT, cuisines{CHAR}: CHAR, menu{CHAR}: CHAR, location: CHAR)
```

This table stores information about every unique restaurant. This includes their menu, budget, type of cuisine and their location. 

```
Purchase(user_id: INT, restaurant_id: INT, purchase_id: INT, date: CHAR, time: CHAR, cost: INT)
ForeignKey(user_id) references User.user_id
ForeignKey(restaurant_id) references Restaurant.restaurant_id
```
This weak entity stores the purchase history at restaurants of every user. 

```
Review(user_id: INT, restaurant_id: INT, review_ID: INT, date: CHAR, rating: INT, description: CHAR)
ForeignKey(user_id) references User.user_id
ForeignKey(restaurant_id) references Restaurant.restaurant_id
```

This table stores reviews of a user. Every user may have multiple reviews of different restaurants. These reviews include the date they were written, rating, and a written section for a specific review. 

### Relations (Raunak)

```
Member_of(user_id, group_id)
PrimaryKey(user_id, group_id)
ForeignKey(user_id) references User.user_id
ForeignKey(group_id) references Groups.group_id
```

This relation keeps track of what users are part of which group. This is a many to many relationship because each group can have multiple users, and each user can be a part of multiple groups.

## Example Queries (Sohan + Raunak)

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
* Python scripts for CSV/Entity generation
* Add more here

### Raunak Bhimsaria

* Example SQL Queries
* Python scripts for CSV/Entity generation
* Add more here
