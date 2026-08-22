// LeetCode 2339 - All the Matches of the League
// https://leetcode.com/problems/all-the-matches-of-the-league/

const char* QUERY =
    "\n"
    "SELECT t1.team_name AS home_team, t2.team_name AS away_team\n"
    "FROM\n"
    "    Teams AS t1\n"
    "    JOIN Teams AS t2\n"
    "WHERE t1.team_name != t2.team_name\n";
