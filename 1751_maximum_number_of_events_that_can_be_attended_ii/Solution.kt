// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

class Solution {
    fun maxValue(events: Array<IntArray>, k: Int): Int {
        val sorted = events.sortedWith(compareBy({ it[0] }, { it[1] }, { it[2] }))
        val n = sorted.size
        val starts = IntArray(n) { sorted[it][0] }

        val dp = Array(k + 1) { IntArray(n + 1) }
        for (i in n - 1 downTo 0) {
            val j = upperBound(starts, sorted[i][1])
            for (remain in 1..k) {
                dp[remain][i] = maxOf(dp[remain][i + 1], sorted[i][2] + dp[remain - 1][j])
            }
        }
        return dp[k][0]
    }

    private fun upperBound(starts: IntArray, target: Int): Int {
        var lo = 0
        var hi = starts.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (starts[mid] <= target) {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        return lo
    }
}
