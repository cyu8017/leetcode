// LeetCode 1412 - Find The Quiet Students In All Exams
// https://leetcode.com/problems/find-the-quiet-students-in-all-exams/

export const QUERY = `SELECT s.student_id, s.student_name
FROM Student s
WHERE EXISTS (SELECT 1 FROM Exam e WHERE e.student_id = s.student_id)
  AND NOT EXISTS (
      SELECT 1
      FROM Exam e
      WHERE e.student_id = s.student_id
        AND (e.score = (SELECT MIN(e2.score) FROM Exam e2 WHERE e2.exam_id = e.exam_id)
          OR e.score = (SELECT MAX(e2.score) FROM Exam e2 WHERE e2.exam_id = e.exam_id))
  )
ORDER BY s.student_id`;
