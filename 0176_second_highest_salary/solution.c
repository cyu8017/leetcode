// LeetCode 0176 - Second Highest Salary
// https://leetcode.com/problems/second-highest-salary/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    (\n"
    "        SELECT DISTINCT salary\n"
    "        FROM Employee\n"
    "        ORDER BY salary DESC\n"
    "        LIMIT 1 OFFSET 1\n"
    "    ) AS SecondHighestSalary\n";