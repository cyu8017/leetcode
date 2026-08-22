// LeetCode 1211 - Queries Quality and Percentage
// https://leetcode.com/problems/queries-quality-and-percentage/

const char* QUERY =
    "\n"
    "SELECT query_name,\n"
    "       ROUND(AVG(rating / position), 2) AS quality,\n"
    "       ROUND(100 * AVG(rating < 3), 2) AS poor_query_percentage\n"
    "FROM Queries\n"
    "GROUP BY query_name\n";
