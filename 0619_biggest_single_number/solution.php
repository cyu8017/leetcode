<?php
// LeetCode 0619 - Biggest Single Number
// https://leetcode.com/problems/biggest-single-number/

const QUERY = <<<'SQL'
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) singles
SQL;
