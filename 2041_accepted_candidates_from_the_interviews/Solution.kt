// LeetCode 2041 - Accepted Candidates From The Interviews
// https://leetcode.com/problems/accepted-candidates-from-the-interviews/

class Solution {
    companion object {
        const val QUERY = "SELECT candidate_id\n" +
            "FROM\n" +
            "    Candidates\n" +
            "    JOIN Rounds USING (interview_id)\n" +
            "WHERE years_of_exp >= 2\n" +
            "GROUP BY 1\n" +
            "HAVING SUM(score) > 15"
    }
}
