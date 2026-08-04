// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution {
    fun minTimeToVisitAllPoints(points: Array<IntArray>): Int {
        var total = 0
        for (i in 1 until points.size) {
            total += maxOf(
                kotlin.math.abs(points[i][0] - points[i - 1][0]),
                kotlin.math.abs(points[i][1] - points[i - 1][1])
            )
        }
        return total
    }
}
