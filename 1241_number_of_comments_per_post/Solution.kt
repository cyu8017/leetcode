// LeetCode 1241 - Number Of Comments Per Post
// https://leetcode.com/problems/number-of-comments-per-post/

class Solution {
    companion object {
        const val QUERY = "SELECT s.sub_id AS post_id, COUNT(DISTINCT c.sub_id) AS number_of_comments\n" +
            "FROM Submissions s\n" +
            "LEFT JOIN Submissions c ON c.parent_id = s.sub_id\n" +
            "WHERE s.parent_id IS NULL\n" +
            "GROUP BY s.sub_id\n" +
            "ORDER BY s.sub_id"
    }
}
