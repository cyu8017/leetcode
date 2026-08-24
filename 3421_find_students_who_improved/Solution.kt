// LeetCode 3421 - Find Students Who Improved
// https://leetcode.com/problems/find-students-who-improved/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    RankedScores AS (\n" +
            "        SELECT\n" +
            "            student_id,\n" +
            "            subject,\n" +
            "            score,\n" +
            "            exam_date,\n" +
            "            ROW_NUMBER() OVER (\n" +
            "                PARTITION BY student_id, subject\n" +
            "                ORDER BY exam_date ASC\n" +
            "            ) AS rn_first,\n" +
            "            ROW_NUMBER() OVER (\n" +
            "                PARTITION BY student_id, subject\n" +
            "                ORDER BY exam_date DESC\n" +
            "            ) AS rn_latest\n" +
            "        FROM Scores\n" +
            "    ),\n" +
            "    FirstAndLatestScores AS (\n" +
            "        SELECT\n" +
            "            f.student_id,\n" +
            "            f.subject,\n" +
            "            f.score AS first_score,\n" +
            "            l.score AS latest_score\n" +
            "        FROM\n" +
            "            RankedScores f\n" +
            "            JOIN RankedScores l ON f.student_id = l.student_id AND f.subject = l.subject\n" +
            "        WHERE f.rn_first = 1 AND l.rn_latest = 1\n" +
            "    )\n" +
            "SELECT\n" +
            "    *\n" +
            "FROM FirstAndLatestScores\n" +
            "WHERE latest_score > first_score\n" +
            "ORDER BY 1, 2;"
    }
}
