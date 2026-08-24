// LeetCode 2338 - Count the Number of Ideal Arrays
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/

class Solution {
    fun idealArrays(n: Int, maxValue: Int): Int {
        val mod = 1_000_000_007
        val maxLen = 14
        val comb = Array(n + 1) { IntArray(maxLen + 1) }
        for (i in 0..n) {
            comb[i][0] = 1
            var j = 1
            while (j <= maxLen && j <= i) {
                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod
                j++
            }
        }
        val dp = Array(maxValue + 1) { IntArray(maxLen + 1) }
        for (i in 1..maxValue) dp[i][1] = 1
        for (len in 2..maxLen) {
            for (v in 1..maxValue) {
                var m = 2 * v
                while (m <= maxValue) {
                    dp[m][len] = (dp[m][len] + dp[v][len - 1]) % mod
                    m += v
                }
            }
        }
        var ans = 0
        for (v in 1..maxValue) {
            var len = 1
            while (len <= maxLen && len <= n) {
                ans = (ans + (dp[v][len].toLong() * comb[n - 1][len - 1] % mod).toInt()) % mod
                len++
            }
        }
        return ans
    }
}
