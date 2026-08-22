// LeetCode 2853 - Highest Salaries Difference
// https://leetcode.com/problems/highest-salaries-difference/

const char* QUERY =
    "\n"
    "SELECT MAX(s) - MIN(s) AS salary_difference\n"
    "FROM\n"
    "    (\n"
    "        SELECT MAX(salary) AS s\n"
    "        FROM Salaries\n"
    "        GROUP BY department\n"
    "    ) AS t\n";
