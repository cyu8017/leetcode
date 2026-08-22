// LeetCode 1613 - Find the Missing IDs
// https://leetcode.com/problems/find-the-missing-ids/

const char* QUERY =
    "\n"
    "WITH RECURSIVE ids AS (\n"
    "  SELECT 1 AS ids\n"
    "  UNION ALL\n"
    "  SELECT ids + 1 FROM ids WHERE ids < (SELECT MAX(customer_id) FROM Customers)\n"
    ")\n"
    "SELECT ids\n"
    "FROM ids\n"
    "WHERE ids NOT IN (SELECT customer_id FROM Customers)\n"
    "ORDER BY ids;\n";
