// LeetCode 0570 - Managers with at Least 5 Direct Reports
// https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

const char* QUERY =
    "\n"
    "SELECT name\n"
    "FROM Employee\n"
    "WHERE id IN (\n"
    "    SELECT managerId\n"
    "    FROM Employee\n"
    "    WHERE managerId IS NOT NULL\n"
    "    GROUP BY managerId\n"
    "    HAVING COUNT(*) >= 5\n"
    ")\n";
