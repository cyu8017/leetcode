// LeetCode 1082 - Sales Analysis I
// https://leetcode.com/problems/sales-analysis-i/

const char* QUERY =
    "\n"
    "SELECT seller_id\n"
    "FROM Sales\n"
    "GROUP BY seller_id\n"
    "HAVING SUM(price) = (\n"
    "    SELECT SUM(price)\n"
    "    FROM Sales\n"
    "    GROUP BY seller_id\n"
    "    ORDER BY SUM(price) DESC\n"
    "    LIMIT 1\n"
    ")\n";
