// LeetCode 2687 - Bikes Last Time Used
// https://leetcode.com/problems/bikes-last-time-used/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    bike_number,\n" +
            "    MAX(end_time) AS end_time\n" +
            "FROM Bikes\n" +
            "GROUP BY bike_number\n" +
            "ORDER BY end_time DESC"
    }
}
