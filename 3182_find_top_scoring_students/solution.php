<?php
// LeetCode 3182 - Find Top Scoring Students
// https://leetcode.com/problems/find-top-scoring-students/

const QUERY = <<<'SQL'
SELECT student_id
FROM
    students
    JOIN courses USING (major)
    LEFT JOIN enrollments USING (student_id, course_id)
GROUP BY 1
HAVING SUM(grade = 'A') = COUNT(major)
ORDER BY 1;
SQL;
