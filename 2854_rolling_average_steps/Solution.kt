// LeetCode 2854 - Rolling Average Steps
// https://leetcode.com/problems/rolling-average-steps/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            steps_date,\n" +
            "            ROUND(\n" +
            "                AVG(steps_count) OVER (\n" +
            "                    PARTITION BY user_id\n" +
            "                    ORDER BY steps_date\n" +
            "                    ROWS 2 PRECEDING\n" +
            "                ),\n" +
            "                2\n" +
            "            ) AS rolling_average,\n" +
            "            DATEDIFF(\n" +
            "                steps_date,\n" +
            "                LAG(steps_date, 2) OVER (\n" +
            "                    PARTITION BY user_id\n" +
            "                    ORDER BY steps_date\n" +
            "                )\n" +
            "            ) = 2 AS st\n" +
            "        FROM Steps\n" +
            "    )\n" +
            "SELECT\n" +
            "    user_id,\n" +
            "    steps_date,\n" +
            "    rolling_average\n" +
            "FROM T\n" +
            "WHERE st = 1\n" +
            "ORDER BY 1, 2"
    }
}
