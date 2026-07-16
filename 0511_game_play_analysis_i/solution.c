// LeetCode 0511 - Game Play Analysis I
// https://leetcode.com/problems/game-play-analysis-i/

const char* QUERY =
    "\n"
    "SELECT player_id, MIN(event_date) AS first_login\n"
    "FROM Activity\n"
    "GROUP BY player_id\n";
