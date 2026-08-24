<?php
// LeetCode 2346 - Compute the Rank as a Percentage
// https://leetcode.com/problems/compute-the-rank-as-a-percentage/

const QUERY = <<<'SQL'
SELECT
    student_id,
    department_id,
    IFNULL(
        ROUND(
            (
                RANK() OVER (
                    PARTITION BY department_id
                    ORDER BY mark DESC
                ) - 1
            ) * 100 / (COUNT(1) OVER (PARTITION BY department_id) - 1),
            2
        ),
        0
    ) AS percentage
FROM Students
SQL;
