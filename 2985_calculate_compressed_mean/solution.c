// LeetCode 2985 - Calculate Compressed Mean
// https://leetcode.com/problems/calculate-compressed-mean/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    ROUND(\n"
    "        SUM(item_count * order_occurrences) / SUM(order_occurrences),\n"
    "        2\n"
    "    ) AS average_items_per_order\n"
    "FROM Orders\n";
