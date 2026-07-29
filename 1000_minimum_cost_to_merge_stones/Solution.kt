// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

class Solution {
    fun mergeStones(stones: IntArray, k: Int): Int {
        val n = stones.size
        if ((n - 1) % (k - 1) != 0) return -1
        val prefix = IntArray(n + 1)
        for (i in 0 until n) prefix[i + 1] = prefix[i] + stones[i]
        val dp = Array(n) { IntArray(n) }
        for (length in k..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                var best = Int.MAX_VALUE / 2
                var m = i
                while (m < j) {
                    best = minOf(best, dp[i][m] + dp[m + 1][j])
                    m += k - 1
                }
                dp[i][j] = best
                if ((length - 1) % (k - 1) == 0) dp[i][j] += prefix[j + 1] - prefix[i]
            }
        }
        return dp[0][n - 1]
    }
}
