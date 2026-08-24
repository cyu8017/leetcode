// LeetCode 0574 - Winning Candidate
// https://leetcode.com/problems/winning-candidate/

class Solution {
    companion object {
        const val QUERY = "SELECT c.name\n" +
            "FROM Candidate c\n" +
            "JOIN Vote v ON c.id = v.candidateId\n" +
            "GROUP BY c.id, c.name\n" +
            "ORDER BY COUNT(*) DESC\n" +
            "LIMIT 1"
    }
}
