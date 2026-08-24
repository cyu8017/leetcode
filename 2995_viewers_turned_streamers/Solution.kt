// LeetCode 2995 - Viewers Turned Streamers
// https://leetcode.com/problems/viewers-turned-streamers/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            session_type,\n" +
            "            RANK() OVER (\n" +
            "                PARTITION BY user_id\n" +
            "                ORDER BY session_start\n" +
            "            ) AS rk\n" +
            "        FROM Sessions\n" +
            "    )\n" +
            "SELECT user_id, COUNT(1) AS sessions_count\n" +
            "FROM\n" +
            "    T AS t\n" +
            "    JOIN Sessions AS s USING (user_id)\n" +
            "WHERE rk = 1 AND t.session_type = 'Viewer' AND s.session_type = 'Streamer'\n" +
            "GROUP BY 1\n" +
            "ORDER BY 2 DESC, 1 DESC"
    }
}
