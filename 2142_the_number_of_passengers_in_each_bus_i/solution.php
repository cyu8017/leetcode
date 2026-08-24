<?php
// LeetCode 2142 - The Number of Passengers in Each Bus I
// https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/

const QUERY = <<<'SQL'
SELECT
    bus_id,
    COUNT(passenger_id) - LAG(COUNT(passenger_id), 1, 0) OVER (
        ORDER BY MIN(b.arrival_time)
    ) AS passengers_cnt
FROM Buses AS b
LEFT JOIN Passengers AS p ON p.arrival_time <= b.arrival_time
GROUP BY bus_id
ORDER BY bus_id
SQL;
