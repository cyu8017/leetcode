// LeetCode 3188 - Find Top Scoring Students Ii
// https://leetcode.com/problems/find-top-scoring-students-ii/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT student_id\n" +
            "        FROM enrollments\n" +
            "        GROUP BY 1\n" +
            "        HAVING AVG(GPA) >= 2.5\n" +
            "    )\n" +
            "SELECT student_id\n" +
            "FROM\n" +
            "    T\n" +
            "    JOIN students USING (student_id)\n" +
            "    JOIN courses USING (major)\n" +
            "    LEFT JOIN enrollments USING (student_id, course_id)\n" +
            "GROUP BY 1\n" +
            "HAVING\n" +
            "    SUM(mandatory = 'yes' AND grade = 'A') = SUM(mandatory = 'yes')\n" +
            "    AND SUM(mandatory = 'no' AND grade IS NOT NULL) = SUM(mandatory = 'no' AND grade IN ('A', 'B'))\n" +
            "    AND SUM(mandatory = 'no' AND grade IS NOT NULL) >= 2\n" +
            "ORDER BY 1;"
    }
}
