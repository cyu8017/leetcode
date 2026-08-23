// LeetCode 0534 - Game Play Analysis III
// https://leetcode.com/problems/game-play-analysis-iii/

const char* QUERY = R"SQL(
SELECT player_id, event_date,
       SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date) AS games_played_so_far
FROM Activity
)SQL";
