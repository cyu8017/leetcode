// LeetCode 1083 - Sales Analysis II
// https://leetcode.com/problems/sales-analysis-ii/

const char* QUERY =
    "\n"
    "SELECT DISTINCT s.buyer_id\n"
    "FROM Sales s\n"
    "JOIN Product p ON s.product_id = p.product_id\n"
    "WHERE p.product_name = 'S8'\n"
    "  AND s.buyer_id NOT IN (\n"
    "      SELECT s2.buyer_id\n"
    "      FROM Sales s2\n"
    "      JOIN Product p2 ON s2.product_id = p2.product_id\n"
    "      WHERE p2.product_name = 'iPhone'\n"
    "  )\n";
