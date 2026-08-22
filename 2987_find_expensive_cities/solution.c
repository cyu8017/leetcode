// LeetCode 2987 - Find Expensive Cities
// https://leetcode.com/problems/find-expensive-cities/

const char* QUERY =
    "\n"
    "SELECT city\n"
    "FROM Listings\n"
    "GROUP BY city\n"
    "HAVING AVG(price) > (SELECT AVG(price) FROM Listings)\n"
    "ORDER BY 1\n";
