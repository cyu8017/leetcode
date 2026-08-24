// LeetCode 1194 - Tournament Winners
// https://leetcode.com/problems/tournament-winners/

class Solution {
    companion object {
        const val QUERY = "WITH scores AS (\n" +
            "    SELECT first_player AS player_id, first_score AS score FROM Matches\n" +
            "    UNION ALL\n" +
            "    SELECT second_player AS player_id, second_score AS score FROM Matches\n" +
            "),\n" +
            "totals AS (\n" +
            "    SELECT p.group_id, p.player_id, COALESCE(SUM(s.score), 0) AS total_score\n" +
            "    FROM Players p\n" +
            "    LEFT JOIN scores s ON p.player_id = s.player_id\n" +
            "    GROUP BY p.group_id, p.player_id\n" +
            ")\n" +
            "SELECT group_id, player_id\n" +
            "FROM (\n" +
            "    SELECT\n" +
            "        group_id,\n" +
            "        player_id,\n" +
            "        ROW_NUMBER() OVER (\n" +
            "            PARTITION BY group_id\n" +
            "            ORDER BY total_score DESC, player_id\n" +
            "        ) AS rn\n" +
            "    FROM totals\n" +
            ") ranked\n" +
            "WHERE rn = 1"
    }
}
