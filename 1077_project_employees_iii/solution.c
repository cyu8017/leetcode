// LeetCode 1077 - Project Employees III
// https://leetcode.com/problems/project-employees-iii/

const char* QUERY =
    "\n"
    "SELECT p.project_id, p.employee_id\n"
    "FROM Project p\n"
    "JOIN Employee e ON p.employee_id = e.employee_id\n"
    "WHERE (p.project_id, e.experience_years) IN (\n"
    "    SELECT p2.project_id, MAX(e2.experience_years)\n"
    "    FROM Project p2\n"
    "    JOIN Employee e2 ON p2.employee_id = e2.employee_id\n"
    "    GROUP BY p2.project_id\n"
    ")\n";
