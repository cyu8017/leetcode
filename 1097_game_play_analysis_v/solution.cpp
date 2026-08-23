// LeetCode 1097 - Game Play Analysis V
// https://leetcode.com/problems/game-play-analysis-v/

const char* QUERY = R"SQL(
SELECT
    install.install_dt,
    COUNT(DISTINCT install.player_id) AS installs,
    ROUND(
        COUNT(DISTINCT activity.player_id) / COUNT(DISTINCT install.player_id),
        2
    ) AS Day1_retention
FROM (
    SELECT player_id, MIN(event_date) AS install_dt
    FROM Activity
    GROUP BY player_id
) install
LEFT JOIN Activity activity
    ON install.player_id = activity.player_id
   AND activity.event_date = DATE_ADD(install.install_dt, INTERVAL 1 DAY)
GROUP BY install.install_dt
)SQL";
