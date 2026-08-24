# LeetCode 2372 - Calculate the Influence of Each Salesperson
# https:# leetcode.com/problems/calculate-the-influence-of-each-salesperson/

# Write your MySQL query statement below
QUERY = """
SELECT sp.salesperson_id, sp.name, IFNULL(SUM(s.price), 0) AS total
FROM Salesperson AS sp
LEFT JOIN Customer AS c ON sp.salesperson_id = c.salesperson_id
LEFT JOIN Sales AS s ON s.customer_id = c.customer_id
GROUP BY sp.salesperson_id, sp.name
"""
