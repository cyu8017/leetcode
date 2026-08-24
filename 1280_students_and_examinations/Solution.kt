// LeetCode 1280 - Students And Examinations
// https://leetcode.com/problems/students-and-examinations/

class Solution {
    companion object {
        const val QUERY = "SELECT s.student_id, s.student_name, sub.subject_name,\n" +
            "       COUNT(e.subject_name) AS attended_exams\n" +
            "FROM Students s\n" +
            "CROSS JOIN Subjects sub\n" +
            "LEFT JOIN Examinations e\n" +
            "  ON e.student_id = s.student_id\n" +
            " AND e.subject_name = sub.subject_name\n" +
            "GROUP BY s.student_id, s.student_name, sub.subject_name\n" +
            "ORDER BY s.student_id, sub.subject_name"
    }
}
