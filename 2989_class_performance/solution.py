# LeetCode 2989 - Class Performance
# https:# leetcode.com/problems/class-performance/

# Write your MySQL query statement below
QUERY = """
SELECT
    MAX(assignment1 + assignment2 + assignment3) - MIN(
        assignment1 + assignment2 + assignment3
    ) AS difference_in_score
FROM Scores
"""
