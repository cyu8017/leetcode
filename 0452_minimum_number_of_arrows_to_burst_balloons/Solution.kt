// LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution {
    fun findMinArrowShots(points: Array<IntArray>): Int {
        if (points.isEmpty()) {
            return 0
        }
        points.sortBy { it[1] }
        var arrows = 1
        var end = points[0][1]
        for (i in 1 until points.size) {
            if (points[i][0] > end) {
                arrows++
                end = points[i][1]
            }
        }
        return arrows
    }
}
