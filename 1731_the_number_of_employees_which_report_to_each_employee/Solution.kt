// LeetCode 1731 - The Number of Employees Which Report to Each Employee
// https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    e.employee_id,\n" +
            "    e.name,\n" +
            "    COUNT(r.employee_id) AS reports_count,\n" +
            "    ROUND(AVG(r.age)) AS average_age\n" +
            "FROM Employees e\n" +
            "JOIN Employees r ON e.employee_id = r.reports_to\n" +
            "GROUP BY e.employee_id, e.name\n" +
            "ORDER BY e.employee_id;\n" +
            ""
    }
}
