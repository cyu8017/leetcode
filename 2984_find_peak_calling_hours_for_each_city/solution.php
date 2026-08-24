<?php
// LeetCode 2984 - Find Peak Calling Hours for Each City
// https://leetcode.com/problems/find-peak-calling-hours-for-each-city/

const QUERY = <<<'SQL'
WITH
    T AS (
        SELECT
            *,
            RANK() OVER (
                PARTITION BY city
                ORDER BY cnt DESC
            ) AS rk
        FROM
            (
                SELECT
                    city,
                    HOUR(call_time) AS h,
                    COUNT(1) AS cnt
                FROM Calls
                GROUP BY 1, 2
            ) AS t
    )
SELECT city, h AS peak_calling_hour, cnt AS number_of_calls
FROM T
WHERE rk = 1
ORDER BY 2 DESC, 1 DESC
SQL;
