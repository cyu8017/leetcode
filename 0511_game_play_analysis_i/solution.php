<?php
// LeetCode 0511 - Game Play Analysis I
// https://leetcode.com/problems/game-play-analysis-i/

const QUERY = <<<'SQL'
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id
SQL;
