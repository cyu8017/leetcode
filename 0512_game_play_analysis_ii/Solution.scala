// LeetCode 0512 - Game Play Analysis II
// https://leetcode.com/problems/game-play-analysis-ii/

object Solution {
  final val QUERY: String = """SELECT a.player_id, a.device_id
FROM Activity a
JOIN (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
) first_login
    ON a.player_id = first_login.player_id
   AND a.event_date = first_login.first_date
"""
}
