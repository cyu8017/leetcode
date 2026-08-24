// LeetCode 3126 - Server Utilization Time
// https://leetcode.com/problems/server-utilization-time/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            session_status,\n" +
            "            status_time,\n" +
            "            LEAD(status_time) OVER (\n" +
            "                PARTITION BY server_id\n" +
            "                ORDER BY status_time\n" +
            "            ) AS next_status_time\n" +
            "        FROM Servers\n" +
            "    )\n" +
            "SELECT FLOOR(SUM(TIMESTAMPDIFF(SECOND, status_time, next_status_time)) / 86400) AS total_uptime_days\n" +
            "FROM T\n" +
            "WHERE session_status = 'start';"
    }
}
