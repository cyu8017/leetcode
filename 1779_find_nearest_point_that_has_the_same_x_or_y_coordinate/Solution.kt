// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution {
    fun nearestValidPoint(x: Int, y: Int, points: Array<IntArray>): Int {
        var best = Int.MAX_VALUE
        var ans = -1
        for (i in points.indices) {
            val px = points[i][0]
            val py = points[i][1]
            if (px != x && py != y) {
                continue
            }
            val dist = Math.abs(px - x) + Math.abs(py - y)
            if (dist < best) {
                best = dist
                ans = i
            }
        }
        return ans
    }
}
