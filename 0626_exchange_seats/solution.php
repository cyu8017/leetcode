<?php
// LeetCode 0626 - Exchange Seats
// https://leetcode.com/problems/exchange-seats/

const QUERY = <<<'SQL'
SELECT
    CASE
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id
        WHEN id % 2 = 1 THEN id + 1
        ELSE id - 1
    END AS id,
    student
FROM Seat
ORDER BY id
SQL;
