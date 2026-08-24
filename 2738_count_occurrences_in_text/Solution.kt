// LeetCode 2738 - Count Occurrences In Text
// https://leetcode.com/problems/count-occurrences-in-text/

class Solution {
    companion object {
        const val QUERY = "SELECT 'bull' AS word, COUNT(*) AS count\n" +
            "FROM Files\n" +
            "WHERE content LIKE '% bull %'\n" +
            "UNION\n" +
            "SELECT 'bear' AS word, COUNT(*) AS count\n" +
            "FROM Files\n" +
            "WHERE content LIKE '% bear %'"
    }
}
