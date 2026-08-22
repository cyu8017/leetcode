// LeetCode 1459 - Rectangles Area
// https://leetcode.com/problems/rectangles-area/

const char* QUERY =
    "\n"
    "SELECT p1.id AS P1, p2.id AS P2,\n"
    "       ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) AS AREA\n"
    "FROM Points p1\n"
    "JOIN Points p2 ON p1.id < p2.id\n"
    "WHERE p1.x_value <> p2.x_value AND p1.y_value <> p2.y_value\n"
    "ORDER BY AREA DESC, P1, P2\n";
