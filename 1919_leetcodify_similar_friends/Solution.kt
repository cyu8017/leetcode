// LeetCode 1919 - Leetcodify Similar Friends
// https://leetcode.com/problems/leetcodify-similar-friends/

class Solution {
    companion object {
        const val QUERY = "WITH listens AS (\n" +
            "  SELECT DISTINCT user_id, song_id, day\n" +
            "  FROM Listens\n" +
            "),\n" +
            "shared AS (\n" +
            "  SELECT\n" +
            "    LEAST(a.user_id, b.user_id) AS user1_id,\n" +
            "    GREATEST(a.user_id, b.user_id) AS user2_id\n" +
            "  FROM listens a\n" +
            "  JOIN listens b\n" +
            "    ON a.day = b.day\n" +
            "   AND a.song_id = b.song_id\n" +
            "   AND a.user_id < b.user_id\n" +
            "  GROUP BY a.user_id, b.user_id, a.day\n" +
            "  HAVING COUNT(*) >= 3\n" +
            ")\n" +
            "SELECT DISTINCT s.user1_id, s.user2_id\n" +
            "FROM shared s\n" +
            "JOIN Friendship f\n" +
            "  ON f.user1_id = s.user1_id\n" +
            " AND f.user2_id = s.user2_id"
    }
}
