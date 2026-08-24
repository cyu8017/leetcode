// LeetCode 3390 - Longest Team Pass Streak
// https://leetcode.com/problems/longest-team-pass-streak/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    PassesWithTeams AS (\n" +
            "        SELECT\n" +
            "            p.pass_from,\n" +
            "            p.pass_to,\n" +
            "            t1.team_name AS team_from,\n" +
            "            t2.team_name AS team_to,\n" +
            "            IF(t1.team_name = t2.team_name, 1, 0) same_team_flag,\n" +
            "            p.time_stamp\n" +
            "        FROM\n" +
            "            Passes p\n" +
            "            JOIN Teams t1 ON p.pass_from = t1.player_id\n" +
            "            JOIN Teams t2 ON p.pass_to = t2.player_id\n" +
            "    ),\n" +
            "    StreakGroups AS (\n" +
            "        SELECT\n" +
            "            team_from AS team_name,\n" +
            "            time_stamp,\n" +
            "            same_team_flag,\n" +
            "            SUM(\n" +
            "                CASE\n" +
            "                    WHEN same_team_flag = 0 THEN 1\n" +
            "                    ELSE 0\n" +
            "                END\n" +
            "            ) OVER (\n" +
            "                PARTITION BY team_from\n" +
            "                ORDER BY time_stamp\n" +
            "            ) AS group_id\n" +
            "        FROM PassesWithTeams\n" +
            "    ),\n" +
            "    StreakLengths AS (\n" +
            "        SELECT\n" +
            "            team_name,\n" +
            "            group_id,\n" +
            "            COUNT(*) AS streak_length\n" +
            "        FROM StreakGroups\n" +
            "        WHERE same_team_flag = 1\n" +
            "        GROUP BY 1, 2\n" +
            "    ),\n" +
            "    LongestStreaks AS (\n" +
            "        SELECT\n" +
            "            team_name,\n" +
            "            MAX(streak_length) AS longest_streak\n" +
            "        FROM StreakLengths\n" +
            "        GROUP BY 1\n" +
            "    )\n" +
            "SELECT\n" +
            "    team_name,\n" +
            "    longest_streak\n" +
            "FROM LongestStreaks\n" +
            "ORDER BY 1;"
    }
}
