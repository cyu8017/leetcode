# LeetCode 2837 - Total Traveled Distance
# https:# leetcode.com/problems/total-traveled-distance/

# Write your MySQL query statement below
QUERY = """
SELECT u.user_id, u.name, IFNULL(SUM(r.distance), 0) AS `traveled distance`
FROM Users AS u
LEFT JOIN Rides AS r USING (user_id)
GROUP BY u.user_id, u.name
ORDER BY u.user_id
"""
