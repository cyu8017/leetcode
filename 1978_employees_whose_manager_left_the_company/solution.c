// LeetCode 1978 - Employees Whose Manager Left the Company
// https://leetcode.com/problems/employees-whose-manager-left-the-company/

const char* QUERY =
    "\n"
    "SELECT employee_id\n"
    "FROM Employees\n"
    "WHERE salary < 30000\n"
    "  AND manager_id IS NOT NULL\n"
    "  AND manager_id NOT IN (SELECT employee_id FROM Employees)\n"
    "ORDER BY employee_id\n";
