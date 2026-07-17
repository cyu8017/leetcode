<?php
// LeetCode 1709 - Biggest Window Between Visits
// https://leetcode.com/problems/biggest-window-between-visits/

const QUERY = <<<'SQL'
SELECT user_id, MAX(DATEDIFF(next_visit, visit_date)) AS biggest_window
FROM (
    SELECT
        user_id,
        visit_date,
        LEAD(visit_date, 1, '2021-1-1') OVER (
            PARTITION BY user_id
            ORDER BY visit_date
        ) AS next_visit
    FROM UserVisits
) AS visits
GROUP BY user_id
ORDER BY user_id;
SQL;
