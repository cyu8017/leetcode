// LeetCode 1112 - Highest Grade For Each Student
// https://leetcode.com/problems/highest-grade-for-each-student/

class Solution {
    companion object {
        const val QUERY = "SELECT student_id, course_id, grade\n" +
            "FROM Enrollments e1\n" +
            "WHERE grade = (\n" +
            "    SELECT MAX(grade)\n" +
            "    FROM Enrollments e2\n" +
            "    WHERE e2.student_id = e1.student_id\n" +
            ")\n" +
            "AND course_id = (\n" +
            "    SELECT MIN(course_id)\n" +
            "    FROM Enrollments e3\n" +
            "    WHERE e3.student_id = e1.student_id\n" +
            "      AND e3.grade = e1.grade\n" +
            ")\n" +
            "ORDER BY student_id"
    }
}
