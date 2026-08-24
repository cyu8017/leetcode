# LeetCode 2314 - The First Day of the Maximum Recorded Degree in Each City
# https:# leetcode.com/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/

# Write your MySQL query statement below
QUERY = """
WITH
    T AS (
        SELECT
            *,
            RANK() OVER (
                PARTITION BY city_id
                ORDER BY degree DESC, day
            ) AS rk
        FROM Weather
    )
SELECT city_id, day, degree
FROM T
WHERE rk = 1
ORDER BY 1
"""
