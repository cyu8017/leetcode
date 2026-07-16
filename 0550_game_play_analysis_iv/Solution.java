// LeetCode 0550 - Game Play Analysis IV
// https://leetcode.com/problems/game-play-analysis-iv/

public class Solution {
    public static final String QUERY = "SELECT ROUND(\n" +
        "    SUM(\n" +
        "        CASE\n" +
        "            WHEN EXISTS (\n" +
        "                SELECT 1\n" +
        "                FROM Activity a\n" +
        "                WHERE a.player_id = f.player_id\n" +
        "                  AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)\n" +
        "            ) THEN 1\n" +
        "            ELSE 0\n" +
        "        END\n" +
        "    ) / COUNT(*),\n" +
        "    2\n" +
        ") AS fraction\n" +
        "FROM (\n" +
        "    SELECT player_id, MIN(event_date) AS first_date\n" +
        "    FROM Activity\n" +
        "    GROUP BY player_id\n" +
        ") f\n";
}
