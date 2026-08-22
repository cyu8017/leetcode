// LeetCode 2084 - Drop Type 1 Orders for Customers With Type 0 Orders
// https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT DISTINCT customer_id\n"
    "        FROM Orders\n"
    "        WHERE order_type = 0\n"
    "    )\n"
    "SELECT *\n"
    "FROM Orders AS o\n"
    "WHERE order_type = 0 OR NOT EXISTS (SELECT 1 FROM T AS t WHERE t.customer_id = o.customer_id)\n";
