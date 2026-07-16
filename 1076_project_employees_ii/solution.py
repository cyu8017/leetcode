# LeetCode 1076 - Project Employees II
# https://leetcode.com/problems/project-employees-ii/

# Write your MySQL query statement below
QUERY = """
SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(*) = (
    SELECT COUNT(*)
    FROM Project
    GROUP BY project_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
"""
