// LeetCode 0790 - Domino and Tromino Tiling
// https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution {
    fun numTilings(n: Int): Int {
        val MOD = 1_000_000_007
        if (n == 1) return 1
        if (n == 2) return 2
        var dp = LongArray(n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for (i in 4 until = n) { dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD }
        return dp[n]
    }
}
