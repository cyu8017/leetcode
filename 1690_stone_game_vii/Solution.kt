// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

class Solution {
    fun stoneGameVII(stones: IntArray): Int {
        val n = stones.size
        val pre = IntArray(n + 1)
        for (i in stones.indices) pre[i + 1] = pre[i] + stones[i]
        val dp = Array(n) { IntArray(n) }
        for (length in 2..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                dp[i][j] = maxOf(
                    pre[j + 1] - pre[i + 1] - dp[i + 1][j],
                    pre[j] - pre[i] - dp[i][j - 1]
                )
            }
        }
        return dp[0][n - 1]
    }
}
