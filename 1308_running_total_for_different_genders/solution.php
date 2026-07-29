<?php
// LeetCode 1308 - Running Total For Different Genders
// https://leetcode.com/problems/running-total-for-different-genders/

const QUERY = <<<'SQL'
SELECT gender, day,
       SUM(score_points) OVER (PARTITION BY gender ORDER BY day) AS total
FROM Scores
ORDER BY gender, day
SQL;
