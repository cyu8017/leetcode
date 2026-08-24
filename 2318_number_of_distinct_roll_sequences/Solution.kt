// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

class Solution {
    private fun gcd(a: Int, b: Int): Int {
        var x = a; var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }

    fun distinctSequences(n: Int): Int {
        val mod = 1_000_000_007
        val dp = Array(n + 1) { Array(7) { IntArray(7) } }
        for (a in 1..6) dp[1][a][0] = 1
        for (i in 2..n) {
            for (prev in 1..6) {
                for (pprev in 0..6) {
                    if (dp[i - 1][prev][pprev] == 0) continue
                    for (cur in 1..6) {
                        if (cur == prev || cur == pprev || gcd(cur, prev) != 1) continue
                        dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % mod
                    }
                }
            }
        }
        var ans = 0
        for (a in 1..6) for (b in 0..6) ans = (ans + dp[n][a][b]) % mod
        return ans
    }
}
