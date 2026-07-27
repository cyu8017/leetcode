// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution {
    fun maxWidthOfVerticalArea(points: Array<IntArray>): Int {
        val xs = points.map { it[0] }.sorted()
        var ans = 0
        for (i in 1 until xs.size) ans = maxOf(ans, xs[i] - xs[i - 1])
        return ans
    }
}
