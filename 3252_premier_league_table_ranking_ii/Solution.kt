// LeetCode 3252 - Premier League Table Ranking Ii
// https://leetcode.com/problems/premier-league-table-ranking-ii/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            team_name,\n" +
            "            wins * 3 + draws AS points,\n" +
            "            RANK() OVER (ORDER BY wins * 3 + draws DESC) AS position,\n" +
            "            COUNT(1) OVER () AS total_teams\n" +
            "        FROM TeamStats\n" +
            "    )\n" +
            "SELECT\n" +
            "    team_name,\n" +
            "    points,\n" +
            "    position,\n" +
            "    CASE\n" +
            "        WHEN position <= CEIL(total_teams / 3.0) THEN 'Tier 1'\n" +
            "        WHEN position <= CEIL(2 * total_teams / 3.0) THEN 'Tier 2'\n" +
            "        ELSE 'Tier 3'\n" +
            "    END tier\n" +
            "FROM T\n" +
            "ORDER BY 2 DESC, 1;"
    }
}
