// LeetCode 1951 - All The Pairs With The Maximum Number Of Common Followers
// https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers/

class Solution {
    companion object {
        const val QUERY = "WITH commons AS (\n" +
            "  SELECT r1.user_id AS user1_id,\n" +
            "         r2.user_id AS user2_id,\n" +
            "         COUNT(*) AS cnt\n" +
            "  FROM Relations r1\n" +
            "  JOIN Relations r2\n" +
            "    ON r1.follower_id = r2.follower_id\n" +
            "   AND r1.user_id < r2.user_id\n" +
            "  GROUP BY r1.user_id, r2.user_id\n" +
            ")\n" +
            "SELECT user1_id, user2_id\n" +
            "FROM commons\n" +
            "WHERE cnt = (SELECT MAX(cnt) FROM commons)"
    }
}
