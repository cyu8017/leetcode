// LeetCode 1406 - Stone Game III
// https://leetcode.com/problems/stone-game-iii/

class Solution {
    fun stoneGameIII(stoneValue: IntArray): String {
        val n = stoneValue.size
        val dp = LongArray(n + 1)
        for (i in n - 1 downTo 0) {
            var take = 0L
            dp[i] = Long.MIN_VALUE / 4
            for (j in i until minOf(i + 3, n)) {
                take += stoneValue[j]
                dp[i] = maxOf(dp[i], take - dp[j + 1])
            }
        }
        return when {
            dp[0] > 0 -> "Alice"
            dp[0] < 0 -> "Bob"
            else -> "Tie"
        }
    }
}
