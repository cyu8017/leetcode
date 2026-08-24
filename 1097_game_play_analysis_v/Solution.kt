// LeetCode 1097 - Game Play Analysis V
// https://leetcode.com/problems/game-play-analysis-v/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    install.install_dt,\n" +
            "    COUNT(DISTINCT install.player_id) AS installs,\n" +
            "    ROUND(\n" +
            "        COUNT(DISTINCT activity.player_id) / COUNT(DISTINCT install.player_id),\n" +
            "        2\n" +
            "    ) AS Day1_retention\n" +
            "FROM (\n" +
            "    SELECT player_id, MIN(event_date) AS install_dt\n" +
            "    FROM Activity\n" +
            "    GROUP BY player_id\n" +
            ") install\n" +
            "LEFT JOIN Activity activity\n" +
            "    ON install.player_id = activity.player_id\n" +
            "   AND activity.event_date = DATE_ADD(install.install_dt, INTERVAL 1 DAY)\n" +
            "GROUP BY install.install_dt"
    }
}
