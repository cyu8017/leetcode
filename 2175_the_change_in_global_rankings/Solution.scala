// LeetCode 2175 - The Change in Global Rankings
// https:// leetcode.com/problems/the-change-in-global-rankings/

object Solution {
  final val QUERY: String = """WITH
    P AS (
        SELECT team_id, SUM(points_change) AS delta
        FROM PointsChange
        GROUP BY team_id
    )
SELECT
    team_id,
    name,
    CAST(RANK() OVER (ORDER BY points DESC, name) AS SIGNED) - CAST(
        RANK() OVER (ORDER BY (points + delta) DESC, name) AS SIGNED
    ) AS 'rank_diff'
FROM
    TeamPoints
    JOIN P USING (team_id)
"""
}
