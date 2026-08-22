// LeetCode 3246 - Premier League Table Ranking
// https://leetcode.com/problems/premier-league-table-ranking/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    team_id,\n"
    "    team_name,\n"
    "    wins * 3 + draws points,\n"
    "    RANK() OVER (ORDER BY (wins * 3 + draws) DESC) position\n"
    "FROM TeamStats\n"
    "ORDER BY 3 DESC, 2;\n";
