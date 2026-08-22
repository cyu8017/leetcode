// LeetCode 1875 - Group Employees of the Same Salary
// https://leetcode.com/problems/group-employees-of-the-same-salary/

const char* QUERY =
    "\n"
    "WITH valid_salaries AS (\n"
    "    SELECT salary\n"
    "    FROM Employees\n"
    "    GROUP BY salary\n"
    "    HAVING COUNT(*) >= 2\n"
    "),\n"
    "ranked AS (\n"
    "    SELECT\n"
    "        salary,\n"
    "        DENSE_RANK() OVER (ORDER BY salary) AS team_id\n"
    "    FROM valid_salaries\n"
    ")\n"
    "SELECT\n"
    "    e.employee_id,\n"
    "    e.name,\n"
    "    e.salary,\n"
    "    r.team_id\n"
    "FROM Employees e\n"
    "JOIN ranked r ON e.salary = r.salary\n"
    "ORDER BY r.team_id, e.employee_id\n";
