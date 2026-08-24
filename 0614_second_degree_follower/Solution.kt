// LeetCode 0614 - Second Degree Follower
// https://leetcode.com/problems/second-degree-follower/

class Solution {
    companion object {
        const val QUERY = "SELECT f1.follower, COUNT(DISTINCT f2.follower) AS num\n" +
            "FROM Follow f1\n" +
            "JOIN Follow f2 ON f1.follower = f2.followee\n" +
            "GROUP BY f1.follower\n" +
            "ORDER BY f1.follower"
    }
}
