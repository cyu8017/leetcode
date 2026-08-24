// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

class Solution {
    fun waysToReachTarget(target: Int, types: Array<IntArray>): Int {
        val MOD = 1_000_000_007
        val dp = IntArray(target + 1)
        dp[0] = 1
        for (t in types) {
            val count = t[0]
            val marks = t[1]
            for (s in target downTo 0) {
                var k = 1
                while (k <= count && s - k * marks >= 0) {
                    dp[s] = (dp[s] + dp[s - k * marks]) % MOD
                    k += 1
                }
            }
        }
        return dp[target]
    }
}
