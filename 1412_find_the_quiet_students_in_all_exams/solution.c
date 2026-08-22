// LeetCode 1412 - Find the Quiet Students in All Exams
// https://leetcode.com/problems/find-the-quiet-students-in-all-exams/

const char* QUERY =
    "\n"
    "SELECT s.student_id, s.student_name\n"
    "FROM Student s\n"
    "WHERE EXISTS (SELECT 1 FROM Exam e WHERE e.student_id = s.student_id)\n"
    "  AND NOT EXISTS (\n"
    "      SELECT 1\n"
    "      FROM Exam e\n"
    "      WHERE e.student_id = s.student_id\n"
    "        AND (e.score = (SELECT MIN(e2.score) FROM Exam e2 WHERE e2.exam_id = e.exam_id)\n"
    "          OR e.score = (SELECT MAX(e2.score) FROM Exam e2 WHERE e2.exam_id = e.exam_id))\n"
    "  )\n"
    "ORDER BY s.student_id\n";
