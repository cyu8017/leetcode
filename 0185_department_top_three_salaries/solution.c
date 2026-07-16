// LeetCode 0185 - Department Top Three Salaries
// https://leetcode.com/problems/department-top-three-salaries/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    d.name AS Department,\n"
    "    e.name AS Employee,\n"
    "    e.salary AS Salary\n"
    "FROM (\n"
    "    SELECT\n"
    "        name,\n"
    "        salary,\n"
    "        departmentId,\n"
    "        DENSE_RANK() OVER (\n"
    "            PARTITION BY departmentId\n"
    "            ORDER BY salary DESC\n"
    "        ) AS salary_rank\n"
    "    FROM Employee\n"
    ") e\n"
    "JOIN Department d ON e.departmentId = d.id\n"
    "WHERE e.salary_rank <= 3\n";