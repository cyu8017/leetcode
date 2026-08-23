// LeetCode 0534 - Game Play Analysis III
// https://leetcode.com/problems/game-play-analysis-iii/

public class Solution
{
    public const string QUERY = "SELECT player_id, event_date,\n" +
        "       SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date) AS games_played_so_far\n" +
        "FROM Activity\n";
}
