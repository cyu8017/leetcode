// LeetCode 1132 - Reported Posts Ii
// https://leetcode.com/problems/reported-posts-ii/

class Solution {
    companion object {
        const val QUERY = "WITH daily AS (\n" +
            "    SELECT\n" +
            "        action_date,\n" +
            "        COUNT(DISTINCT post_id) AS reported,\n" +
            "        COUNT(DISTINCT CASE WHEN r.post_id IS NOT NULL THEN a.post_id END) AS removed\n" +
            "    FROM Actions a\n" +
            "    LEFT JOIN Removals r ON a.post_id = r.post_id\n" +
            "    WHERE a.action = 'report' AND a.extra = 'spam'\n" +
            "    GROUP BY action_date\n" +
            ")\n" +
            "SELECT ROUND(AVG(removed * 100.0 / reported), 2) AS average_daily_percent\n" +
            "FROM daily"
    }
}
