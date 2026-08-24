// LeetCode 1194 - Tournament Winners
// https://leetcode.com/problems/tournament-winners/

let QUERY = """
WITH scores AS (
    SELECT first_player AS player_id, first_score AS score FROM Matches
    UNION ALL
    SELECT second_player AS player_id, second_score AS score FROM Matches
),
totals AS (
    SELECT p.group_id, p.player_id, COALESCE(SUM(s.score), 0) AS total_score
    FROM Players p
    LEFT JOIN scores s ON p.player_id = s.player_id
    GROUP BY p.group_id, p.player_id
)
SELECT group_id, player_id
FROM (
    SELECT
        group_id,
        player_id,
        ROW_NUMBER() OVER (
            PARTITION BY group_id
            ORDER BY total_score DESC, player_id
        ) AS rn
    FROM totals
) ranked
WHERE rn = 1
"""
