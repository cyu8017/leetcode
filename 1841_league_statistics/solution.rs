// LeetCode 1841 - League Statistics
// https://leetcode.com/problems/league-statistics/

const QUERY: &str = r#"
WITH HomeStats AS (
    SELECT
        home_team_id AS team_id,
        1 AS matches_played,
        CASE
            WHEN home_team_goals > away_team_goals THEN 3
            WHEN home_team_goals = away_team_goals THEN 1
            ELSE 0
        END AS points,
        home_team_goals AS goal_for,
        away_team_goals AS goal_against
    FROM Matches
),
AwayStats AS (
    SELECT
        away_team_id AS team_id,
        1 AS matches_played,
        CASE
            WHEN away_team_goals > home_team_goals THEN 3
            WHEN away_team_goals = home_team_goals THEN 1
            ELSE 0
        END AS points,
        away_team_goals AS goal_for,
        home_team_goals AS goal_against
    FROM Matches
),
Combined AS (
    SELECT * FROM HomeStats
    UNION ALL
    SELECT * FROM AwayStats
),
Aggregated AS (
    SELECT
        team_id,
        SUM(matches_played) AS matches_played,
        SUM(points) AS points,
        SUM(goal_for) AS goal_for,
        SUM(goal_against) AS goal_against
    FROM Combined
    GROUP BY team_id
)
SELECT
    t.team_name,
    a.matches_played,
    a.points,
    a.goal_for,
    a.goal_against,
    a.goal_for - a.goal_against AS goal_diff
FROM Teams t
JOIN Aggregated a ON t.team_id = a.team_id
ORDER BY a.points DESC, goal_diff DESC, t.team_name ASC
"#;
