// LeetCode 0730 - Count Different Palindromic Subsequences
// https://leetcode.com/problems/count-different-palindromic-subsequences/

class Solution {
    fun countPalindromicSubsequences(s: String): Int {
        val mod = 1000000007
        var n = s.length
        var dp = Array(n) { LongArray(n) }
        for (i in 0 until n) { dp[i][i] = 1 }
        for (length in 2 ..n) {
            for (i in 0 ..n - length) {
                var j = i + length - 1
                if (s[i] != s[j]) dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                else {
                    var left = i + 1
                    var right = j - 1
                    while (left <= right && s[left] != s[i]) left++
                    while (left <= right && s[right] != s[i]) right--
                    if (left > right) dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    else if (left == right) dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]
                }
                dp[i][j] = (dp[i][j] % mod + mod) % mod
            }
        }
        return dp[0][n - 1]
    }
}
