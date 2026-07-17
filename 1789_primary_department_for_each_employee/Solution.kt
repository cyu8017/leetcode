// LeetCode 1789 - Primary Department for Each Employee
// https://leetcode.com/problems/primary-department-for-each-employee/

class Solution {
    companion object {
        const val QUERY = "SELECT employee_id, department_id\n" +
            "FROM Employee\n" +
            "WHERE primary_flag = 'Y'\n" +
            "   OR employee_id IN (\n" +
            "       SELECT employee_id FROM Employee GROUP BY employee_id HAVING COUNT(*) = 1\n" +
            "   );\n" +
            ""
    }
}
