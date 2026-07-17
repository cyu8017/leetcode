// LeetCode 1783 - Grand Slam Titles
// https://leetcode.com/problems/grand-slam-titles/

const QUERY: &str = r#"
SELECT p.player_id, p.player_name, COUNT(*) AS grand_slams_count
FROM Players p
JOIN (
    SELECT Wimbledon AS player_id FROM Championships
    UNION ALL SELECT Fr_open FROM Championships
    UNION ALL SELECT US_open FROM Championships
    UNION ALL SELECT Au_open FROM Championships
) w ON p.player_id = w.player_id
GROUP BY p.player_id, p.player_name;
"#;
