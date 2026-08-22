// LeetCode 3052 - Maximize Items
// https://leetcode.com/problems/maximize-items/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT SUM(square_footage) AS s\n"
    "        FROM Inventory\n"
    "        WHERE item_type = 'prime_eligible'\n"
    "    )\n"
    "SELECT\n"
    "    'prime_eligible' AS item_type,\n"
    "    COUNT(1) * FLOOR(500000 / s) AS item_count\n"
    "FROM\n"
    "    Inventory\n"
    "    JOIN T\n"
    "WHERE item_type = 'prime_eligible'\n"
    "UNION ALL\n"
    "SELECT\n"
    "    'not_prime',\n"
    "    IFNULL(COUNT(1) * FLOOR(IF(s = 0, 500000, 500000 % s) / SUM(square_footage)), 0)\n"
    "FROM\n"
    "    Inventory\n"
    "    JOIN T\n"
    "WHERE item_type = 'not_prime';\n";
