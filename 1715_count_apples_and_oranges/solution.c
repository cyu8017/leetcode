// LeetCode 1715 - Count Apples and Oranges
// https://leetcode.com/problems/count-apples-and-oranges/

const char* QUERY =
    "\n"
    "SELECT SUM(apple_count) AS apple_count, SUM(orange_count) AS orange_count\n"
    "FROM (\n"
    "    SELECT apple_count, orange_count FROM Boxes\n"
    "    UNION ALL\n"
    "    SELECT apple_count, orange_count\n"
    "    FROM Chests\n"
    "    WHERE chest_id IN (SELECT chest_id FROM Boxes WHERE chest_id IS NOT NULL)\n"
    ") AS counts;\n";
