// LeetCode 0613 - Shortest Distance In A Line
// https://leetcode.com/problems/shortest-distance-in-a-line/

class Solution {
    companion object {
        const val QUERY = "SELECT MIN(ABS(p1.x - p2.x)) AS shortest\n" +
            "FROM Point p1\n" +
            "JOIN Point p2 ON p1.x < p2.x"
    }
}
