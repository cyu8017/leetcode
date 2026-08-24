// LeetCode 3156 - Employee Task Duration And Concurrent Tasks
// https://leetcode.com/problems/employee-task-duration-and-concurrent-tasks/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT DISTINCT employee_id, start_time AS st\n" +
            "        FROM Tasks\n" +
            "        UNION DISTINCT\n" +
            "        SELECT DISTINCT employee_id, end_time AS st\n" +
            "        FROM Tasks\n" +
            "    ),\n" +
            "    P AS (\n" +
            "        SELECT\n" +
            "            *,\n" +
            "            LEAD(st) OVER (\n" +
            "                PARTITION BY employee_id\n" +
            "                ORDER BY st\n" +
            "            ) AS ed\n" +
            "        FROM T\n" +
            "    ),\n" +
            "    S AS (\n" +
            "        SELECT\n" +
            "            P.*,\n" +
            "            COUNT(1) AS concurrent_count\n" +
            "        FROM\n" +
            "            P\n" +
            "            INNER JOIN Tasks USING (employee_id)\n" +
            "        WHERE P.st >= Tasks.start_time AND P.ed <= Tasks.end_time\n" +
            "        GROUP BY 1, 2, 3\n" +
            "    )\n" +
            "SELECT\n" +
            "    employee_id,\n" +
            "    FLOOR(SUM(TIME_TO_SEC(TIMEDIFF(ed, st)) / 3600)) AS total_task_hours,\n" +
            "    MAX(concurrent_count) AS max_concurrent_tasks\n" +
            "FROM S\n" +
            "GROUP BY 1\n" +
            "ORDER BY 1;"
    }
}
