# LeetCode 2687 - Bikes Last Time Used
# https:# leetcode.com/problems/bikes-last-time-used/

# Write your MySQL query statement below
QUERY = """
SELECT
    bike_number,
    MAX(end_time) AS end_time
FROM Bikes
GROUP BY bike_number
ORDER BY end_time DESC
"""
