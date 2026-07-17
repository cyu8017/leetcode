// LeetCode 1729 - Find Followers Count
// https://leetcode.com/problems/find-followers-count/

class Solution {
    companion object {
        const val QUERY = "SELECT user_id, COUNT(follower_id) AS followers_count\n" +
            "FROM Followers\n" +
            "GROUP BY user_id\n" +
            "ORDER BY user_id;\n" +
            ""
    }
}
