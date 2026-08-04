// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

class Solution {
    fun minCost(n: Int, cuts: IntArray): Int {
        val points = mutableListOf(0)
        for (c in cuts) points.add(c)
        points.add(n)
        points.sort()
        val size = points.size
        val dp = Array(size) { IntArray(size) }
        for (width in 2 until size) {
            for (left in 0 until size - width) {
                val right = left + width
                var best = Int.MAX_VALUE / 4
                for (mid in left + 1 until right) {
                    best = minOf(best, dp[left][mid] + dp[mid][right])
                }
                best = if (right > left + 1) best + points[right] - points[left] else 0
                dp[left][right] = best
            }
        }
        return dp[0][size - 1]
    }
}
