// LeetCode 0183 - Customers Who Never Order
// https://leetcode.com/problems/customers-who-never-order/

const char* QUERY =
    "\n"
    "SELECT name AS Customers\n"
    "FROM Customers\n"
    "WHERE id NOT IN (\n"
    "    SELECT customerId\n"
    "    FROM Orders\n"
    ")\n";