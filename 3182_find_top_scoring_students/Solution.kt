// LeetCode 3182 - Find Top Scoring Students
// https://leetcode.com/problems/find-top-scoring-students/

class Solution {
    companion object {
        const val QUERY = "SELECT student_id\n" +
            "FROM\n" +
            "    students\n" +
            "    JOIN courses USING (major)\n" +
            "    LEFT JOIN enrollments USING (student_id, course_id)\n" +
            "GROUP BY 1\n" +
            "HAVING SUM(grade = 'A') = COUNT(major)\n" +
            "ORDER BY 1;"
    }
}
