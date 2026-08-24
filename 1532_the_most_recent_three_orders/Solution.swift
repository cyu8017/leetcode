// LeetCode 1532 - The Most Recent Three Orders
// https://leetcode.com/problems/the-most-recent-three-orders/

let QUERY = """
SELECT c.name AS customer_name, c.customer_id, o.order_id, o.order_date
FROM Customers c
JOIN Orders o ON o.customer_id = c.customer_id
WHERE (
    SELECT COUNT(*)
    FROM Orders o2
    WHERE o2.customer_id = o.customer_id
      AND (o2.order_date > o.order_date OR (o2.order_date = o.order_date AND o2.order_id > o.order_id))
) < 3
ORDER BY c.name, c.customer_id, o.order_date DESC
"""
