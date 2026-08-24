// LeetCode 1264 - Page Recommendations
// https://leetcode.com/problems/page-recommendations/

class Solution {
    companion object {
        const val QUERY = "SELECT DISTINCT page_id AS recommended_page\n" +
            "FROM Likes\n" +
            "WHERE user_id IN (\n" +
            "    SELECT user2_id FROM Friendship WHERE user1_id = 1\n" +
            "    UNION\n" +
            "    SELECT user1_id FROM Friendship WHERE user2_id = 1\n" +
            ")\n" +
            "AND page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)"
    }
}
