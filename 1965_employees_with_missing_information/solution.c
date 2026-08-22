// LeetCode 1965 - Employees With Missing Information
// https://leetcode.com/problems/employees-with-missing-information/

const char* QUERY =
    "\n"
    "SELECT employee_id\n"
    "FROM Employees\n"
    "WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)\n"
    "UNION\n"
    "SELECT employee_id\n"
    "FROM Salaries\n"
    "WHERE employee_id NOT IN (SELECT employee_id FROM Employees)\n"
    "ORDER BY 1\n";
