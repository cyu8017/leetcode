// LeetCode 0183 - Customers Who Never Order
// https://leetcode.com/problems/customers-who-never-order/

let QUERY = """
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
)
"""