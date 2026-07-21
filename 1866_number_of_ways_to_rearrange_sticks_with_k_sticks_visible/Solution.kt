// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

class Solution {
    fun rearrangeSticks(n: Int, k: Int): Int {
        val mod = 1_000_000_007
        if (k == 0 || k > n) return 0
        val dp = Array(n + 1) { LongArray(n + 1) }
        dp[1][1] = 1
        for (sticks in 2..n) {
            dp[sticks][1] = (sticks - 1L) * dp[sticks - 1][1] % mod
            for (visible in 2..sticks) {
                dp[sticks][visible] = (
                    dp[sticks - 1][visible - 1] + (sticks - 1L) * dp[sticks - 1][visible]
                ) % mod
            }
        }
        return dp[n][k].toInt()
    }
}
