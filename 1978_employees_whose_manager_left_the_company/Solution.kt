// LeetCode 1978 - Employees Whose Manager Left The Company
// https://leetcode.com/problems/employees-whose-manager-left-the-company/

class Solution {
    companion object {
        const val QUERY = "SELECT employee_id\n" +
            "FROM Employees\n" +
            "WHERE salary < 30000\n" +
            "  AND manager_id IS NOT NULL\n" +
            "  AND manager_id NOT IN (SELECT employee_id FROM Employees)\n" +
            "ORDER BY employee_id"
    }
}
