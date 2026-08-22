// LeetCode 1421 - NPV Queries
// https://leetcode.com/problems/npv-queries/

const char* QUERY =
    "\n"
    "SELECT q.id, q.year, COALESCE(n.npv, 0) AS npv\n"
    "FROM Queries q\n"
    "LEFT JOIN NPV n ON n.id = q.id AND n.year = q.year\n";
