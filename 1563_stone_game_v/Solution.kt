// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/

class Solution {
    fun stoneGameV(stoneValue: IntArray): Int {
        val n = stoneValue.size
        if (n == 0) return 0
        val pre = IntArray(n + 1)
        for (i in 0 until n) pre[i + 1] = pre[i] + stoneValue[i]
        val dp = Array(n) { IntArray(n) }
        val left = Array(n) { IntArray(n) }
        val right = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            left[i][i] = stoneValue[i]
            right[i][i] = stoneValue[i]
        }
        for (length in 2..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                var lo = i
                var hi = j - 1
                while (lo <= hi) {
                    val mid = (lo + hi) ushr 1
                    if (2L * (pre[mid + 1] - pre[i]) >= pre[j + 1] - pre[i]) hi = mid - 1 else lo = mid + 1
                }
                val split = lo
                val leftSum = pre[split + 1] - pre[i]
                val rightSum = pre[j + 1] - pre[split + 1]
                var best = right[split + 1][j]
                if (leftSum == rightSum) {
                    best = maxOf(best, left[i][split])
                } else if (split > i) {
                    best = maxOf(best, left[i][split - 1])
                }
                dp[i][j] = best
                val total = pre[j + 1] - pre[i]
                left[i][j] = maxOf(left[i][j - 1], total + best)
                right[i][j] = maxOf(right[i + 1][j], total + best)
            }
        }
        return dp[0][n - 1]
    }
}
