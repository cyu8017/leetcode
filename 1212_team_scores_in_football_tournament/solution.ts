// LeetCode 1212 - Team Scores In Football Tournament
// https://leetcode.com/problems/team-scores-in-football-tournament/

export const QUERY = `SELECT team_id, team_name,
       SUM(CASE WHEN team_id = host_team THEN
                    CASE WHEN host_goals > guest_goals THEN 3 WHEN host_goals = guest_goals THEN 1 ELSE 0 END
                ELSE CASE WHEN guest_goals > host_goals THEN 3 WHEN guest_goals = host_goals THEN 1 ELSE 0 END END) AS num_points
FROM Teams
LEFT JOIN Matches ON team_id IN (host_team, guest_team)
GROUP BY team_id, team_name
ORDER BY num_points DESC, team_id`;
