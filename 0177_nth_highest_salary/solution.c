// LeetCode 0177 - Nth Highest Salary
// https://leetcode.com/problems/nth-highest-salary/

const char* QUERY =
    "\n"
    "CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT\n"
    "BEGIN\n"
    "  DECLARE M INT;\n"
    "  SET M = N - 1;\n"
    "  RETURN (\n"
    "    SELECT DISTINCT salary\n"
    "    FROM Employee\n"
    "    ORDER BY salary DESC\n"
    "    LIMIT 1 OFFSET M\n"
    "  );\n"
    "END\n";