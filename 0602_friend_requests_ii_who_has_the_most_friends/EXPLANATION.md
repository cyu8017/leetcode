# How We Solve Friend Requests II: Who Has the Most Friends

Count each user as both requester and accepter, then take the maximum.

## Steps

1. Union requester ids with accepter ids.
2. Group by id and count appearances.
3. Return the id with the largest count.
