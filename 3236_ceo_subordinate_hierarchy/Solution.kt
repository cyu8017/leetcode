// LeetCode 3236 - Ceo Subordinate Hierarchy
// https://leetcode.com/problems/ceo-subordinate-hierarchy/

class Solution {
    companion object {
        const val QUERY = "WITH RECURSIVE\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            employee_id,\n" +
            "            employee_name,\n" +
            "            0 AS hierarchy_level,\n" +
            "            manager_id,\n" +
            "            salary\n" +
            "        FROM Employees\n" +
            "        WHERE manager_id IS NULL\n" +
            "        UNION ALL\n" +
            "        SELECT\n" +
            "            e.employee_id,\n" +
            "            e.employee_name,\n" +
            "            hierarchy_level + 1 AS hierarchy_level,\n" +
            "            e.manager_id,\n" +
            "            e.salary\n" +
            "        FROM\n" +
            "            T t\n" +
            "            JOIN Employees e ON t.employee_id = e.manager_id\n" +
            "    ),\n" +
            "    P AS (\n" +
            "        SELECT salary\n" +
            "        FROM Employees\n" +
            "        WHERE manager_id IS NULL\n" +
            "    )\n" +
            "SELECT\n" +
            "    employee_id subordinate_id,\n" +
            "    employee_name subordinate_name,\n" +
            "    hierarchy_level,\n" +
            "    t.salary - p.salary salary_difference\n" +
            "FROM\n" +
            "    T t\n" +
            "    JOIN P p\n" +
            "WHERE hierarchy_level != 0\n" +
            "ORDER BY 3, 1;"
    }
}
