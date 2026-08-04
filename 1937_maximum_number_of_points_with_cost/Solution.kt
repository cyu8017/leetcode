// LeetCode 1937
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution {
    fun maxPoints(points: Array<IntArray>): Long {
        val m = points.size
        val n = points[0].size
        var dp = LongArray(n) { points[0][it].toLong() }
        for (r in 1 until m) {
            val left = LongArray(n)
            val right = LongArray(n)
            left[0] = dp[0]
            for (c in 1 until n) left[c] = maxOf(left[c - 1] - 1, dp[c])
            right[n - 1] = dp[n - 1]
            for (c in n - 2 downTo 0) right[c] = maxOf(right[c + 1] - 1, dp[c])
            dp = LongArray(n) { c -> points[r][c] + maxOf(left[c], right[c]) }
        }
        return dp.maxOrNull()!!
    }
}
