// LeetCode 3322 - Premier League Table Ranking III
// https://leetcode.com/problems/premier-league-table-ranking-iii/

class Solution {
    public static final String QUERY = """
SELECT
    season_id,
    team_id,
    team_name,
    wins * 3 + draws points,
    goals_for - goals_against goal_difference,
    RANK() OVER (
        PARTITION BY season_id
        ORDER BY wins * 3 + draws DESC, goals_for - goals_against DESC, team_name
    ) position
FROM SeasonStats
ORDER BY 1, 6, 3;
""";
}
