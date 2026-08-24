// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

class Solution {
    fun probabilityOfHeads(prob: DoubleArray, target: Int): Double {
        val dp = DoubleArray(target + 1)
        dp[0] = 1.0
        for (p in prob) {
            for (heads in target downTo 0) {
                dp[heads] = dp[heads] * (1 - p) + if (heads > 0) dp[heads - 1] * p else 0.0
            }
        }
        return dp[target]
    }
}
