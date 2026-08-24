// LeetCode 1949 - Strong Friendship
// https://leetcode.com/problems/strong-friendship/

class Solution {
    companion object {
        const val QUERY = "WITH F AS (\n" +
            "  SELECT user1_id, user2_id FROM Friendship\n" +
            "  UNION ALL\n" +
            "  SELECT user2_id, user1_id FROM Friendship\n" +
            ")\n" +
            "SELECT a.user1_id, a.user2_id, COUNT(*) AS common_friend\n" +
            "FROM Friendship a\n" +
            "JOIN F b ON a.user1_id = b.user1_id\n" +
            "JOIN F c ON a.user2_id = c.user1_id AND b.user2_id = c.user2_id\n" +
            "GROUP BY a.user1_id, a.user2_id\n" +
            "HAVING COUNT(*) >= 3"
    }
}
