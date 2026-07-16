# How We Solve Second Degree Follower

A second-degree follower both follows someone and has followers of their own.

## Steps

1. Join `Follow` to itself on `follower = followee`.
2. Group by that shared user and count distinct followers.
3. Order the names alphabetically.
