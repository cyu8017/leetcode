<?php
// LeetCode 1875 - Group Employees of the Same Salary
// https://leetcode.com/problems/group-employees-of-the-same-salary/

const QUERY = <<<'SQL'
WITH valid_salaries AS (
    SELECT salary
    FROM Employees
    GROUP BY salary
    HAVING COUNT(*) >= 2
),
ranked AS (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary) AS team_id
    FROM valid_salaries
)
SELECT
    e.employee_id,
    e.name,
    e.salary,
    r.team_id
FROM Employees e
JOIN ranked r ON e.salary = r.salary
ORDER BY r.team_id, e.employee_id
SQL;
