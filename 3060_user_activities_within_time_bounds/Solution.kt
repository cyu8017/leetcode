// LeetCode 3060 - User Activities Within Time Bounds
// https://leetcode.com/problems/user-activities-within-time-bounds/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            session_start,\n" +
            "            LAG(session_end) OVER (\n" +
            "                PARTITION BY user_id, session_type\n" +
            "                ORDER BY session_end\n" +
            "            ) AS prev_session_end\n" +
            "        FROM Sessions\n" +
            "    )\n" +
            "SELECT DISTINCT\n" +
            "    user_id\n" +
            "FROM T\n" +
            "WHERE TIMESTAMPDIFF(HOUR, prev_session_end, session_start) <= 12;"
    }
}
