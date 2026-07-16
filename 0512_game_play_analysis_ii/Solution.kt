// LeetCode 0512 - Game Play Analysis II
// https://leetcode.com/problems/game-play-analysis-ii/

class Solution {
    companion object {
        const val QUERY = "SELECT a.player_id, a.device_id\n" +
            "FROM Activity a\n" +
            "JOIN (\n" +
            "    SELECT player_id, MIN(event_date) AS first_date\n" +
            "    FROM Activity\n" +
            "    GROUP BY player_id\n" +
            ") first_login\n" +
            "    ON a.player_id = first_login.player_id\n" +
            "   AND a.event_date = first_login.first_date\n"
    }
}
