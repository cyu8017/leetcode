// LeetCode 0184 - Department Highest Salary
// https://leetcode.com/problems/department-highest-salary/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    d.name AS Department,\n"
    "    e.name AS Employee,\n"
    "    e.salary AS Salary\n"
    "FROM Employee e\n"
    "JOIN Department d ON e.departmentId = d.id\n"
    "WHERE e.salary = (\n"
    "    SELECT MAX(salary)\n"
    "    FROM Employee\n"
    "    WHERE departmentId = e.departmentId\n"
    ")\n";