// LeetCode 2175 - The Change in Global Rankings
// https://leetcode.com/problems/the-change-in-global-rankings/

const char* QUERY =
    "\n"
    "WITH\n"
    "    P AS (\n"
    "        SELECT team_id, SUM(points_change) AS delta\n"
    "        FROM PointsChange\n"
    "        GROUP BY team_id\n"
    "    )\n"
    "SELECT\n"
    "    team_id,\n"
    "    name,\n"
    "    CAST(RANK() OVER (ORDER BY points DESC, name) AS SIGNED) - CAST(\n"
    "        RANK() OVER (ORDER BY (points + delta) DESC, name) AS SIGNED\n"
    "    ) AS 'rank_diff'\n"
    "FROM\n"
    "    TeamPoints\n"
    "    JOIN P USING (team_id)\n";
