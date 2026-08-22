// LeetCode 3384 - Team Dominance by Pass Success
// https://leetcode.com/problems/team-dominance-by-pass-success/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT\n"
    "            t1.team_name,\n"
    "            IF(time_stamp <= '45:00', 1, 2) half_number,\n"
    "            IF(t1.team_name = t2.team_name, 1, -1) dominance\n"
    "        FROM\n"
    "            Passes p\n"
    "            JOIN Teams t1 ON p.pass_from = t1.player_id\n"
    "            JOIN Teams t2 ON p.pass_to = t2.player_id\n"
    "    )\n"
    "SELECT team_name, half_number, SUM(dominance) dominance\n"
    "FROM T\n"
    "GROUP BY 1, 2\n"
    "ORDER BY 1, 2;\n";
