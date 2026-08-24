// LeetCode 3482 - Analyze Organization Hierarchy
// https://leetcode.com/problems/analyze-organization-hierarchy/

class Solution {
    companion object {
        const val QUERY = "WITH RECURSIVE\n" +
            "    level_cte AS (\n" +
            "        SELECT employee_id, manager_id, 1 AS level, salary FROM Employees\n" +
            "        UNION ALL\n" +
            "        SELECT a.employee_id, b.manager_id, level + 1, a.salary\n" +
            "        FROM\n" +
            "            level_cte a\n" +
            "            JOIN Employees b ON b.employee_id = a.manager_id\n" +
            "    ),\n" +
            "    employee_with_level AS (\n" +
            "        SELECT a.employee_id, a.employee_name, a.salary, b.level\n" +
            "        FROM\n" +
            "            Employees a,\n" +
            "            (SELECT employee_id, level FROM level_cte WHERE manager_id IS NULL) b\n" +
            "        WHERE a.employee_id = b.employee_id\n" +
            "    )\n" +
            "SELECT\n" +
            "    a.employee_id,\n" +
            "    a.employee_name,\n" +
            "    a.level,\n" +
            "    COALESCE(b.team_size, 0) AS team_size,\n" +
            "    a.salary + COALESCE(b.budget, 0) AS budget\n" +
            "FROM\n" +
            "    employee_with_level a\n" +
            "    LEFT JOIN (\n" +
            "        SELECT manager_id AS employee_id, COUNT(*) AS team_size, SUM(salary) AS budget\n" +
            "        FROM level_cte\n" +
            "        WHERE manager_id IS NOT NULL\n" +
            "        GROUP BY manager_id\n" +
            "    ) b\n" +
            "        ON a.employee_id = b.employee_id\n" +
            "ORDER BY level, budget DESC, employee_name;"
    }
}
