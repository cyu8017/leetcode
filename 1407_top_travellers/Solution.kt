// LeetCode 1407 - Top Travellers
// https://leetcode.com/problems/top-travellers/

class Solution {
    companion object {
        const val QUERY = "SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance\n" +
            "FROM Users u\n" +
            "LEFT JOIN Rides r ON r.user_id = u.id\n" +
            "GROUP BY u.id, u.name\n" +
            "ORDER BY travelled_distance DESC, u.name ASC"
    }
}
