// LeetCode 0578 - Get Highest Answer Rate Question
// https://leetcode.com/problems/get-highest-answer-rate-question/

class Solution {
    companion object {
        const val QUERY = "SELECT question_id AS survey_log\n" +
            "FROM SurveyLog\n" +
            "GROUP BY question_id\n" +
            "ORDER BY\n" +
            "    SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) * 1.0 /\n" +
            "    NULLIF(SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END), 0) DESC,\n" +
            "    question_id ASC\n" +
            "LIMIT 1"
    }
}
