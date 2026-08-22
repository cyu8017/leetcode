// LeetCode 0607 - Sales Person
// https://leetcode.com/problems/sales-person/

const char* QUERY =
    "\n"
    "SELECT name\n"
    "FROM SalesPerson\n"
    "WHERE sales_id NOT IN (\n"
    "    SELECT o.sales_id\n"
    "    FROM Orders o\n"
    "    JOIN Company c ON o.com_id = c.com_id\n"
    "    WHERE c.name = 'RED'\n"
    ")\n";
