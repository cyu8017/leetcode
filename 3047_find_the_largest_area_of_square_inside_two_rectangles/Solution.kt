// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

class Solution {
    fun largestSquareArea(bottomLeft: Array<IntArray>, topRight: Array<IntArray>): Long {
        var ans = 0
        var n = bottomLeft.size
        for (i in 0 until n) {
            var x1 = bottomLeft[i][0]
            var y1 = bottomLeft[i][1]
            var x2 = topRight[i][0]
            var y2 = topRight[i][1]
            for (j in i + 1 until n) {
                var x3 = bottomLeft[j][0]
                var y3 = bottomLeft[j][1]
                var x4 = topRight[j][0]
                var y4 = topRight[j][1]
                var ww = minOf(x2, x4) - maxOf(x1, x3)
                var h = minOf(y2, y4) - maxOf(y1, y3)
                var e = minOf(ww, h)
                if (e > 0) ans = maxOf(ans, e * e)
            }
        }
        return ans
    }
}
