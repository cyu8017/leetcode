// LeetCode 3322 - Premier League Table Ranking Iii
// https://leetcode.com/problems/premier-league-table-ranking-iii/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    season_id,\n" +
            "    team_id,\n" +
            "    team_name,\n" +
            "    wins * 3 + draws points,\n" +
            "    goals_for - goals_against goal_difference,\n" +
            "    RANK() OVER (\n" +
            "        PARTITION BY season_id\n" +
            "        ORDER BY wins * 3 + draws DESC, goals_for - goals_against DESC, team_name\n" +
            "    ) position\n" +
            "FROM SeasonStats\n" +
            "ORDER BY 1, 6, 3;"
    }
}
