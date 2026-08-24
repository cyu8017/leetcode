# LeetCode 3415 - Find Products with Three Consecutive Digits
# https:# leetcode.com/problems/find-products-with-three-consecutive-digits/

# Write your MySQL query statement below
QUERY = """
SELECT product_id, name
FROM Products
WHERE name REGEXP '(^|[^0-9])[0-9]{3}([^0-9]|$)'
ORDER BY 1;
"""
