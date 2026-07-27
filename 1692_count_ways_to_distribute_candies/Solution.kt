// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

class Solution {
    fun waysToDistribute(n: Int, k: Int): Int {
        val mod = 1_000_000_007
        val dp = LongArray(k + 1)
        dp[0] = 1
        for (i in 1..n) {
            for (j in minOf(i, k) downTo 1) {
                dp[j] = (dp[j - 1] + j * dp[j]) % mod
            }
            dp[0] = 0
        }
        return dp[k].toInt()
    }
}
