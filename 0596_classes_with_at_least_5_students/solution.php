<?php
// LeetCode 0596 - Classes With At Least 5 Students
// https://leetcode.com/problems/classes-with-at-least-5-students/

const QUERY = <<<'SQL'
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5
SQL;
