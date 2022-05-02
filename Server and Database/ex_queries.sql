# Query 1: Find the top 5 restaurants that serve the favorite cuisine of the user
SELECT r.name, r.address, r.city
FROM restaurant r, rescuisine rc, user u, usercuisine uc, review re
WHERE u.userID = 'U1006' AND u.userID = uc.userID AND r.placeID = rc.placeID AND uc.cuisine = rc.cuisine 
                     AND r.placeID = re.placeID
GROUP BY r.placeID
ORDER BY (AVG(re.rating))DESC LIMIT 5;

# Query 2: Find the least-encountered (newer) restaurants for a group based on their preference
SELECT r.name, r.address, r.city
FROM restaurant r, community c, purchase p, rescuisine rc, groupmembers gm
WHERE c.groupID = 1 AND r.placeID = rc.placeID AND rc.cuisine = c.cuisine_overlap AND c.groupID = gm.groupID AND gm.userID = p.userID
GROUP BY r.placeID
ORDER BY (SELECT COUNT(p.purchaseID)) LIMIT 5;

# Query 3: Find the top 5 closest restaurants that fit the budget for every member in the group
SELECT r.name, r.address, r.city
FROM restaurant r, Community c
WHERE c.groupID = 1 AND c.min_budget >= r.price
ORDER BY (POW((r.longitude-c.midLong),2) + POW((r.latitude-c.midLat),2)) LIMIT 5;

# Query 4: Find the 5 most open-minded user in terms of preferred cuisines
SELECT u.userID
FROM user u, usercuisine uc
WHERE u.userID = uc.userID
GROUP BY u.userID
ORDER BY (COUNT(uc.cuisine))DESC LIMIT 5;

# Query 5: Find the most frivolous user (user that has spent the most money)
SELECT u.userID
FROM user u, restaurant r, purchase p
WHERE u.userID = p.userID AND r.placeID and p.placeID
GROUP BY u.userID
ORDER BY (SUM(p.cost))DESC LIMIT 1;

# Query 6: Find all the restaurants that serve wine, are wheelchair accessable, have a low price budget, and have an informal dress-code
SELECT r.name
FROM restaurant r
WHERE r.price = 1 AND r.dress_code = "informal" AND r.alcohol = "Wine-Beer" AND r.accessibility = "completely"