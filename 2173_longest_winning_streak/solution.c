// LeetCode 2173 - Longest Winning Streak
// https://leetcode.com/problems/longest-winning-streak/

const char* QUERY =
    "\n"
    "WITH\n"
    "    S AS (\n"
    "        SELECT\n"
    "            *,\n"
    "            ROW_NUMBER() OVER (\n"
    "                PARTITION BY player_id\n"
    "                ORDER BY match_day\n"
    "            ) - ROW_NUMBER() OVER (\n"
    "                PARTITION BY player_id, result\n"
    "                ORDER BY match_day\n"
    "            ) AS rk\n"
    "        FROM Matches\n"
    "    ),\n"
    "    T AS (\n"
    "        SELECT player_id, SUM(result = 'Win') AS s\n"
    "        FROM S\n"
    "        GROUP BY player_id, rk\n"
    "    )\n"
    "SELECT player_id, MAX(s) AS longest_streak\n"
    "FROM T\n"
    "GROUP BY player_id\n";
