// LeetCode 2668 - Find Latest Salaries
// https://leetcode.com/problems/find-latest-salaries/

class Solution {
    companion object {
        const val QUERY = "SELECT emp_id, firstname, lastname, salary, department_id\n" +
            "FROM Salary\n" +
            "WHERE (emp_id, salary) IN (\n" +
            "    SELECT emp_id, MAX(salary)\n" +
            "    FROM Salary\n" +
            "    GROUP BY emp_id\n" +
            ")\n" +
            "ORDER BY emp_id"
    }
}
