# LeetCode 3198 - Find Cities in Each State
# https:# leetcode.com/problems/find-cities-in-each-state/

# Write your MySQL query statement below
QUERY = """
SELECT
    state,
    GROUP_CONCAT(city ORDER BY city SEPARATOR ', ') cities
FROM cities
GROUP BY 1
ORDER BY 1;
"""
