// LeetCode 3057 - Employees Project Allocation
// https://leetcode.com/problems/employees-project-allocation/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT team, AVG(workload) AS avg_workload\n" +
            "        FROM\n" +
            "            Project\n" +
            "            JOIN Employees USING (employee_id)\n" +
            "        GROUP BY 1\n" +
            "    )\n" +
            "SELECT\n" +
            "    employee_id,\n" +
            "    project_id,\n" +
            "    name AS employee_name,\n" +
            "    workload AS project_workload\n" +
            "FROM\n" +
            "    Project\n" +
            "    JOIN Employees USING (employee_id)\n" +
            "    JOIN T USING (team)\n" +
            "WHERE workload > avg_workload\n" +
            "ORDER BY 1, 2;"
    }
}
