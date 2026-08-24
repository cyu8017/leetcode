// LeetCode 1270 - All People Report To The Given Manager
// https://leetcode.com/problems/all-people-report-to-the-given-manager/

class Solution {
    companion object {
        const val QUERY = "WITH RECURSIVE reports AS (\n" +
            "    SELECT employee_id\n" +
            "    FROM Employees\n" +
            "    WHERE manager_id = 1 AND employee_id <> 1\n" +
            "    UNION ALL\n" +
            "    SELECT e.employee_id\n" +
            "    FROM Employees e\n" +
            "    JOIN reports r ON e.manager_id = r.employee_id\n" +
            ")\n" +
            "SELECT employee_id\n" +
            "FROM reports\n" +
            "WHERE employee_id <> 1"
    }
}
