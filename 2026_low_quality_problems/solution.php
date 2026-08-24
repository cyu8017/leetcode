<?php
// LeetCode 2026 - Low-Quality Problems
// https://leetcode.com/problems/low-quality-problems/

const QUERY = <<<'SQL'
SELECT problem_id
FROM Problems
WHERE likes / (likes + dislikes) < 0.6
ORDER BY problem_id
SQL;
