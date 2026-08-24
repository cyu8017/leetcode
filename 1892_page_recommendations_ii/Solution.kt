// LeetCode 1892 - Page Recommendations Ii
// https://leetcode.com/problems/page-recommendations-ii/

class Solution {
    companion object {
        const val QUERY = "SELECT f.user_id, l.page_id, COUNT(*) AS friends_likes\n" +
            "FROM (\n" +
            "    SELECT user1_id AS user_id, user2_id AS friend_id FROM Friendship\n" +
            "    UNION ALL\n" +
            "    SELECT user2_id AS user_id, user1_id AS friend_id FROM Friendship\n" +
            ") f\n" +
            "JOIN Likes l ON l.user_id = f.friend_id\n" +
            "LEFT JOIN Likes ul ON ul.user_id = f.user_id AND ul.page_id = l.page_id\n" +
            "WHERE ul.page_id IS NULL\n" +
            "GROUP BY f.user_id, l.page_id"
    }
}
