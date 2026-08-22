// LeetCode 0569 - Median Employee Salary
// https://leetcode.com/problems/median-employee-salary/

const char* QUERY =
    "\n"
    "SELECT id, company, salary\n"
    "FROM (\n"
    "    SELECT\n"
    "        id,\n"
    "        company,\n"
    "        salary,\n"
    "        ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary, id) AS rn,\n"
    "        COUNT(*) OVER (PARTITION BY company) AS cnt\n"
    "    FROM Employee\n"
    ") ranked\n"
    "WHERE rn = FLOOR((cnt + 1) / 2)\n"
    "   OR rn = FLOOR(cnt / 2) + 1\n";
