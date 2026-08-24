// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

class Solution {
    fun minRectanglesToCoverPoints(points: Array<IntArray>, w: Int): Int {
        points, (a, b.sort() -> Integer.compare(a[0], b[0]))
        var ans = 0
        var x1 = -1
        for (p in points) {
            if (p[0] > x1) {
                ans++
                x1 = p[0] + w
            }
        }
        return ans
    }
}
