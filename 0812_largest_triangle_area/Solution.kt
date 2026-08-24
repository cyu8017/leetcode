// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

class Solution {
    fun largestTriangleArea(points: Array<IntArray>): Double {
        var best = 0.0
        var n = points.size
        for (i in 0 until n) {
            var x1 = points[i][0]
            var y1 = points[i][1]
            for (j in i + 1 until n) {
                var x2 = points[j][0]
                var y2 = points[j][1]
                for (k in j + 1 until n) {
                    var x3 = points[k][0]
                    var y3 = points[k][1]
                    var area = kotlin.math.abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
                    best = maxOf(best, area)
                }
            }
        }
        return best
    }
}
