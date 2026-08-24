<?php
// LeetCode 1965 - Employees With Missing Information
// https://leetcode.com/problems/employees-with-missing-information/

const QUERY = <<<'SQL'
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY 1
SQL;
