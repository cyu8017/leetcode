// LeetCode 0183 - Customers Who Never Order
// https://leetcode.com/problems/customers-who-never-order/

const char* QUERY = R"SQL(
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
)
)SQL";