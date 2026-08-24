// LeetCode 1212 - Team Scores In Football Tournament
// https://leetcode.com/problems/team-scores-in-football-tournament/

class Solution {
    companion object {
        const val QUERY = "SELECT team_id, team_name,\n" +
            "       SUM(CASE WHEN team_id = host_team THEN\n" +
            "                    CASE WHEN host_goals > guest_goals THEN 3 WHEN host_goals = guest_goals THEN 1 ELSE 0 END\n" +
            "                ELSE CASE WHEN guest_goals > host_goals THEN 3 WHEN guest_goals = host_goals THEN 1 ELSE 0 END END) AS num_points\n" +
            "FROM Teams\n" +
            "LEFT JOIN Matches ON team_id IN (host_team, guest_team)\n" +
            "GROUP BY team_id, team_name\n" +
            "ORDER BY num_points DESC, team_id"
    }
}
