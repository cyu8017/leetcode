# LeetCode 1112 - Highest Grade For Each Student
# https:# leetcode.com/problems/highest-grade-for-each-student/

QUERY = <<~SQL
  SELECT student_id, course_id, grade
  FROM Enrollments e1
  WHERE grade = (
      SELECT MAX(grade)
      FROM Enrollments e2
      WHERE e2.student_id = e1.student_id
  )
  AND course_id = (
      SELECT MIN(course_id)
      FROM Enrollments e3
      WHERE e3.student_id = e1.student_id
        AND e3.grade = e1.grade
  )
  ORDER BY student_id
SQL
