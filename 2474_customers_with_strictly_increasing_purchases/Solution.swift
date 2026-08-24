// LeetCode 2474 - Customers With Strictly Increasing Purchases
// https://leetcode.com/problems/customers-with-strictly-increasing-purchases/

let QUERY = """
SELECT customer_id
FROM (
    SELECT
        customer_id,
        yr,
        total,
        yr - RANK() OVER (
            PARTITION BY customer_id
            ORDER BY total
        ) AS rk
    FROM (
        SELECT customer_id, YEAR(order_date) AS yr, SUM(price) AS total
        FROM Orders
        GROUP BY customer_id, YEAR(order_date)
    ) AS s
) AS t
GROUP BY customer_id
HAVING COUNT(DISTINCT rk) = 1
"""
