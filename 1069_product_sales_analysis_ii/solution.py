# LeetCode 1069 - Product Sales Analysis II
# https://leetcode.com/problems/product-sales-analysis-ii/

# Write your MySQL query statement below
QUERY = """
SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id
"""
