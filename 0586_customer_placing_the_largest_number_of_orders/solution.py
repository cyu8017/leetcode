# LeetCode 0586 - Customer Placing the Largest Number of Orders
# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

QUERY = """
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1
"""
