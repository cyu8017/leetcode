// LeetCode 0612 - Shortest Distance In A Plane
// https://leetcode.com/problems/shortest-distance-in-a-plane/

class Solution {
    companion object {
        const val QUERY = "SELECT ROUND(\n" +
            "    MIN(SQRT(POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2))),\n" +
            "    2\n" +
            ") AS shortest\n" +
            "FROM Point2D p1\n" +
            "JOIN Point2D p2\n" +
            "    ON p1.x < p2.x OR (p1.x = p2.x AND p1.y < p2.y)"
    }
}
